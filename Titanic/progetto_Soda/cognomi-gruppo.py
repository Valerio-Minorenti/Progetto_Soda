import pandas as pd

# Carica il CSV
df = pd.read_csv("train.csv")

# Estrai gruppo (parte prima dell'underscore) e cognome (ultima parola del nome)
df['Group'] = df['PassengerId'].str.split('_').str[0]
df['Surname'] = df['Name'].str.split().str[-1]

# Filtra righe valide (senza valori mancanti per Group o Surname)
df_valid = df.dropna(subset=['Group', 'Surname'])

# Seleziona solo gruppi con almeno 2 persone
group_counts = df_valid['Group'].value_counts()
valid_groups = group_counts[group_counts >= 2].index
df_filtered = df_valid[df_valid['Group'].isin(valid_groups)]

# Conta gruppi totali e quelli in cui tutti hanno lo stesso cognome
total_groups = 0
same_surname_groups = 0

for group_id, group_df in df_filtered.groupby('Group'):
    total_groups += 1
    if group_df['Surname'].nunique() == 1:
        same_surname_groups += 1

# Calcola la percentuale
percentage = (same_surname_groups / total_groups) * 100 if total_groups > 0 else 0

# Stampa i risultati
print(f"Numero totale di gruppi con almeno 2 persone: {total_groups}")
print(f"Numero di gruppi con tutti i membri con lo stesso cognome: {same_surname_groups}")
print(f"Percentuale: {percentage:.2f}%")
