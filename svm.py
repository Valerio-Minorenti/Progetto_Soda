import pandas as pd
import joblib
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

def svm(df_train_encoded, df_val_encoded):
 
    target = 'Transported'
    X_train = df_train_encoded.drop(columns=[target])
    y_train = df_train_encoded[target]

    X_val = df_val_encoded.drop(columns=[target])
    y_val = df_val_encoded[target]


    # Crea il modello SVM con kernel lineare (puoi cambiare il kernel se necessario)
    model = SVC(kernel='linear', random_state=42)

    # Allena il modello
    model.fit(X_train, y_train)

    # Predici con i dati di test
    y_pred = model.predict(X_val)

    # Calcola l'accuratezza
    acc = accuracy_score(y_val, y_pred)
    report = classification_report(y_val, y_pred)

    # Stampa i risultati
    print(f"Accuracy: {acc:.4f}")
    print(report)

    return model