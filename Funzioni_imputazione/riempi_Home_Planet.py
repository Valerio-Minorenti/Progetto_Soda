import pandas as pd

def riempi_Home_Planet(df):
    # Assicura che la colonna 'Group' esista
    if 'Group' not in df.columns:
        df['Group'] = df['PassengerId'].str.split('_').str[0].astype(int)

    # Crea una tabella con il valore più frequente di HomePlanet per ogni Group (moda)
    planet_group= df.dropna(subset=['HomePlanet']).groupby('Group')['HomePlanet'].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else pd.NA)

    # Trova gli indici dei passeggeri con HomePlanet mancante e Group presente in GHP_gb
    riempi = df[(df['HomePlanet'].isna()) & (df['Group'].isin(planet_group.index))].index

    # Riempie i valori mancanti con la moda del gruppo
    df.loc[riempi, 'HomePlanet'] = df.loc[riempi, 'Group'].map(planet_group)

    # Conta i missing values dopo
    missing_aft = df['HomePlanet'].isna().sum()

    print('#HomePlanet missing values after:', missing_aft)

    # Joint distribution of CabinDeck and HomePlanet
CDHP_gb=data.groupby(['Deck','HomePlanet'])['HomePlanet'].size().unstack().fillna(0)

# Heatmap of missing values
plt.figure(figsize=(10,4))
sns.heatmap(CDHP_gb.T, annot=True, fmt='g', cmap='coolwarm')

# Missing values before
HP_bef=data['HomePlanet'].isna().sum()

# Decks A, B, C or T came from Europa
data.loc[(data['HomePlanet'].isna()) & (data['Deck'].isin(['A', 'B', 'C', 'T'])), 'HomePlanet']='Europa'

# Deck G came from Earth
data.loc[(data['HomePlanet'].isna()) & (data['Deck']=='G'), 'HomePlanet']='Earth'

# Print number of missing values left
print('#HomePlanet missing values before:',HP_bef)
print('#HomePlanet missing values after:',data['HomePlanet'].isna().sum())

# Joint distribution of Surname and HomePlanet
SHP_gb=data.groupby(['Surname','HomePlanet'])['HomePlanet'].size().unstack().fillna(0)

# Countplot of unique values
plt.figure(figsize=(10,4))
sns.countplot((SHP_gb>0).sum(axis=1))
plt.title('Number of unique planets per surname')

# Missing values before
HP_bef=data['HomePlanet'].isna().sum()

# Passengers with missing HomePlanet and in a family with known HomePlanet
SHP_index=data[data['HomePlanet'].isna()][(data[data['HomePlanet'].isna()]['Surname']).isin(SHP_gb.index)].index

# Fill corresponding missing values
data.loc[SHP_index,'HomePlanet']=data.iloc[SHP_index,:]['Surname'].map(lambda x: SHP_gb.idxmax(axis=1)[x])

# Print number of missing values left
print('#HomePlanet missing values before:',HP_bef)
print('#HomePlanet missing values after:',data['HomePlanet'].isna().sum())

    return df
