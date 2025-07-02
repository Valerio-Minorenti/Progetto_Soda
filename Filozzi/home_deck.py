import pandas as pd

# Legge il file Excel
df = pd.read_excel("train_cabin.xlsx")

# Rimuove righe con valori nulli in Num, HomePlanet o Destination
df_filtrato = df.dropna(subset=['Num', 'HomePlanet', 'Destination']).copy()

# Distribuzione percentuale dei pianeti di partenza per ciascun Num
distribuzione_homeplanet = (
    df_filtrato.groupby('Num')['HomePlanet']
    .value_counts(normalize=True)
    .mul(100)
    .rename('Percentuale')
    .reset_index()
)

# Distribuzione percentuale delle destinazioni per ciascun Num
distribuzione_destination = (
    df_filtrato.groupby('Num')['Destination']
    .value_counts(normalize=True)
    .mul(100)
    .rename('Percentuale')
    .reset_index()
)

# Output
print("Distribuzione HomePlanet per Num (%):")
print(distribuzione_homeplanet)

print("\nDistribuzione Destination per Num (%):")
print(distribuzione_destination)
