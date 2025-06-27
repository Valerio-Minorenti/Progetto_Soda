import pandas as pd

# Carica il CSV
df = pd.read_csv("train.csv")

# Estrai il cognome
df['Surname'] = df['Name'].str.split().str[-1]

# Filtra righe valide con HomePlanet e Surname
df_valid = df.dropna(subset=['Surname', 'HomePlanet'])

# Raggruppa per cognome (famiglia)
total_families = 0
same_planet_families = 0
 
for surname, group_df in df_valid.groupby('Surname'):
    if len(group_df) >= 2:  # Consideriamo solo famiglie (almeno 2 persone)
        total_families += 1
        if group_df['HomePlanet'].nunique() == 1:
            same_planet_families += 1

# Calcola percentuale
if total_families > 0:
    percentage = (same_planet_families / total_families) * 100
else:
    percentage = 0

# Stampa i risultati
print(f"Numero totale di famiglie (cognomi con almeno 2 persone): {total_families}")
print(f"Numero di famiglie in cui tutti i membri provengono dallo stesso pianeta: {same_planet_families}")
print(f"Percentuale di famiglie dallo stesso pianeta: {percentage:.2f}%")
