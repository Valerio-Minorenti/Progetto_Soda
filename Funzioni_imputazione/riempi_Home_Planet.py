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

    return df
