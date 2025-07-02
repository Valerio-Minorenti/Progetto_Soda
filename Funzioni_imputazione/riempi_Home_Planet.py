import pandas as pd

def riempi_Home_Planet(df):
    if 'Group' not in df.columns:
        df['Group'] = df['PassengerId'].str.split('_').str[0].astype(int)

    gruppi_multipli = df['Group'].value_counts()
    gruppi_validi = gruppi_multipli[gruppi_multipli > 1].index

    homeplanet_gruppo = (
        df[df['Group'].isin(gruppi_validi)]
        .dropna(subset=['HomePlanet'])
        .groupby('Group')['HomePlanet']
        .agg(lambda x: x.mode()[0] if x.nunique() == 1 else None)
        .dropna()
        .to_dict()
    )

    df['HomePlanet'] = df.apply(
        lambda row: homeplanet_gruppo.get(row['Group'], row['HomePlanet']) if pd.isna(row['HomePlanet']) else row['HomePlanet'],
        axis=1
    )

    return df
