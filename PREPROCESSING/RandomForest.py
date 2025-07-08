import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

def custom_preprocess(df):
    df['Group'] = df['PassengerId'].apply(lambda x: x.split('_')[0]).astype(int)
    df['Group_size'] = df['Group'].map(df['Group'].value_counts())
    df['Surname'] = df['Name'].str.split().str[-1]
    df[['Deck', 'CabinNum', 'Side']] = df['Cabin'].str.split('/', expand=True)
    df['CabinNum'] = pd.to_numeric(df['CabinNum'], errors='coerce')
    df['Expendures'] = df[['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']].sum(axis=1)
    df['Expendures'] = (df['Expendures'] > df['Expendures'].median()).astype(int)
    df['Solo'] = (df['Group_size'] == 1).astype(int)
    df['UniqueSurname'] = df['Surname'].map(lambda x: 1 if pd.notna(x) and df['Surname'].tolist().count(x) == 1 else 0)
    df['Cabin_region1'] = (df['CabinNum'] < 300).astype(int)
    df['Cabin_region2'] = ((df['CabinNum'] >= 300) & (df['CabinNum'] < 600)).astype(int)
    df['Cabin_region3'] = ((df['CabinNum'] >= 600) & (df['CabinNum'] < 900)).astype(int)
    df['Cabin_region4'] = ((df['CabinNum'] >= 900) & (df['CabinNum'] < 1200)).astype(int)
    df['Cabin_region5'] = ((df['CabinNum'] >= 1200) & (df['CabinNum'] < 1500)).astype(int)
    df['Cabin_region6'] = ((df['CabinNum'] >= 1500) & (df['CabinNum'] < 1800)).astype(int)
    df['Cabin_region7'] = (df['CabinNum'] >= 1800).astype(int)
    df = df.drop(columns=['Name', 'Cabin', 'Surname', 'PassengerId', 'Group'], errors='ignore')
    df = pd.get_dummies(df, columns=['HomePlanet', 'CryoSleep', 'Destination', 'VIP', 'Deck', 'Side'], drop_first=True)
    return df

def train_random_forest(input_csv, model_output_path='rf_model.pkl'):
    df = pd.read_csv(input_csv)
    df = custom_preprocess(df)
    target = 'Transported'
    X = df.drop(columns=[target])
    y = df[target].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, max_depth=8, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    joblib.dump(model, model_output_path)

    print(f"Accuracy: {acc:.4f}")
    print(report)
    print(f"Modello salvato in: {model_output_path}")
