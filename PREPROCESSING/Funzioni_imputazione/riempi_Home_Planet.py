def riempi_Home_Planet(df):
    # Assicura che la colonna 'Group' esista
    if 'Group' not in df.columns:
        df['Group'] = df['PassengerId'].str.split('_').str[0].astype(int)

    # Gruppi con più di una persona
    gruppi_multipli = df['Group'].value_counts()
    gruppi_validi = gruppi_multipli[gruppi_multipli > 1].index

    # Crea un dizionario con il valore di HomePlanet se è unico per il gruppo (tra i valori non nulli)
    homeplanet_gruppo = (
        df[df['Group'].isin(gruppi_validi)]
        .dropna(subset=['HomePlanet'])
        .groupby('Group')['HomePlanet']
        .agg(lambda x: x.mode()[0] if x.nunique() == 1 else None)
        .dropna()
        .to_dict()
    )

    # Riempie i valori mancanti
    df['HomePlanet'] = df.apply(
        lambda row: homeplanet_gruppo.get(row['Group'], row['HomePlanet']) if pd.isna(row['HomePlanet']) else row['HomePlanet'],
        axis=1
    )

    return df
