import pandas as pd

# Legge il file Excel
df = pd.read_excel("train_cabin.xlsx")

# Rimuove righe con valori nulli in Deck, HomePlanet o Destination
df_filtrato = df.dropna(subset=['Deck', 'HomePlanet', 'Destination']).copy()

# Distribuzione percentuale dei pianeti di partenza per ciascun Deck
distribuzione_homeplanet = (
    df_filtrato.groupby('Deck')['HomePlanet']
    .value_counts(normalize=True)
    .mul(100)
    .rename('Percentuale')
    .reset_index()
)

# Distribuzione percentuale delle destinazioni per ciascun Deck
distribuzione_destination = (
    df_filtrato.groupby('Deck')['Destination']
    .value_counts(normalize=True)
    .mul(100)
    .rename('Percentuale')
    .reset_index()
)

# Output
print("Distribuzione HomePlanet per Deck (%):")
print(distribuzione_homeplanet)

print("\nDistribuzione Destination per Deck (%):")
print(distribuzione_destination)
