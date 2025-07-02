import pandas as pd

# Legge il file Excel
df = pd.read_excel("train_cabin.xlsx")

# Estrae il cognome
df['Surname'] = df['Name'].str.split().str[-1]

# Rimuove righe con Surname, Destination o HomePlanet nulli
df_filtrato = df.dropna(subset=['Surname', 'Destination', 'HomePlanet']).copy()

# Distribuzione percentuale delle destinazioni per ciascun cognome
distribuzione_dest = (
    df_filtrato.groupby('Surname')['Destination']
    .value_counts(normalize=True)
    .mul(100)
    .rename('Percentuale')
    .reset_index()
)

# Distribuzione percentuale della provenienza per ciascun cognome
distribuzione_home = (
    df_filtrato.groupby('Surname')['HomePlanet']
    .value_counts(normalize=True)
    .mul(100)
    .rename('Percentuale')
    .reset_index()
)

# Output
print("Distribuzione Destination per Cognome (%):")
print(distribuzione_dest)

print("\nDistribuzione HomePlanet per Cognome (%):")
print(distribuzione_home)
