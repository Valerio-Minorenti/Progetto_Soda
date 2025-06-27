import pandas as pd

# Carica il CSV
df = pd.read_csv("train.csv")

# Estrai il gruppo dalla PassengerId
df['Group'] = df['PassengerId'].str.split('_').str[0]

# Filtra righe con valori validi
df_valid = df.dropna(subset=['Group', 'HomePlanet'])

# Raggruppa per gruppo
total_groups = 0
same_planet_groups = 0

for group_id, group_df in df_valid.groupby('Group'):
    if len(group_df) >= 2:  # Considera solo gruppi con almeno 2 membri
        total_groups += 1
        if group_df['HomePlanet'].nunique() == 1:
            same_planet_groups += 1

# Calcola percentuale
if total_groups > 0:
    percentage = (same_planet_groups / total_groups) * 100
else:
    percentage = 0

# Stampa i risultati
print(f"Numero totale di gruppi (con almeno 2 persone): {total_groups}")
print(f"Numero di gruppi con tutti i membri dallo stesso pianeta: {same_planet_groups}")
print(f"Percentuale di gruppi dallo stesso pianeta: {percentage:.2f}%")
