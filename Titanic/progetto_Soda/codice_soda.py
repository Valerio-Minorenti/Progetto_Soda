import pandas as pd

# Percorso del file CSV
file_path = 'C:/Users/Standard/Desktop/progetto_Soda/train.csv'  

# Caricamento del file
df = pd.read_csv(file_path)

# Estrazione dei pianeti unici, escludendo 'Earth' e 'Europa'
home_planets = df['Destination'].dropna().unique()
altri_pianeti = [p for p in home_planets if p not in ['TRAPPIST-1e', '55 Cancri e']]

# Stampa dei risultati
print("Pianeti presenti oltre a Earth ed Europa:")
for pianeta in altri_pianeti:
    print(pianeta)
