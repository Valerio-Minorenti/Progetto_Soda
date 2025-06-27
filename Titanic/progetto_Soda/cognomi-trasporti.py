import pandas as pd

# Carica il CSV
df = pd.read_csv("train.csv")

# Estrai il cognome
df['Surname'] = df['Name'].str.split().str[-1]

# Filtra righe valide con cognome e stato di trasporto
df_valid = df.dropna(subset=['Surname', 'Transported'])

# Raggruppa per cognome (famiglia)
total_families = 0
same_transport_families = 0

for surname, group_df in df_valid.groupby('Surname'):
    if len(group_df) >= 2:  # Considera solo famiglie con almeno 2 membri
        total_families += 1
        if group_df['Transported'].nunique() == 1:
            same_transport_families += 1

# Calcola percentuale
if total_families > 0:
    percentage = (same_transport_families / total_families) * 100
else:
    percentage = 0

# Stampa i risultati
print(f"Numero totale di famiglie (cognomi con almeno 2 persone): {total_families}")
print(f"Numero di famiglie con stato di trasporto uguale per tutti i membri: {same_transport_families}")
print(f"Percentuale di famiglie con trasporto coerente: {percentage:.2f}%")
