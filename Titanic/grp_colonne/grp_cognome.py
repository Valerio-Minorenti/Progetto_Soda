import pandas as pd

# Legge il file Excel
df = pd.read_excel("train_cabin.xlsx")

# Estrae il gruppo
df['Group'] = df['PassengerId'].str.split('_').str[0]

# Estrae il cognome (ultima parola del campo Name)
df['Surname'] = df['Name'].str.split().str[-1]

# Rimuove righe con Surname nullo
df = df.dropna(subset=['Surname'])

# Seleziona solo gruppi con almeno 2 persone
group_sizes = df['Group'].value_counts()
gruppi_validi = group_sizes[group_sizes >= 2].index
df_filtrato = df[df['Group'].isin(gruppi_validi)].copy()

# Verifica per ogni gruppo se ha un solo cognome
gruppi_con_singolo_cognome = (
    df_filtrato.groupby('Group')['Surname']
    .agg(lambda x: x.nunique() == 1)
)

# Mappa il risultato su ciascun passeggero
mappa_cognomi_gruppi = gruppi_con_singolo_cognome.to_dict()
df_filtrato['Stesso_Cognome'] = df_filtrato['Group'].map(mappa_cognomi_gruppi)

# Calcola la percentuale di persone in gruppi con cognome condiviso
percentuale = df_filtrato['Stesso_Cognome'].sum() / len(df_filtrato) * 100
print(round(percentuale, 2))
