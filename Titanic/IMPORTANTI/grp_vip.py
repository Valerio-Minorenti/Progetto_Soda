import pandas as pd

# Legge il file Excel
df = pd.read_excel("train_cabin.xlsx")

# Estrae il gruppo
df['Group'] = df['PassengerId'].str.split('_').str[0]

# Conta dimensione dei gruppi
group_sizes = df['Group'].value_counts()
gruppi_validi = group_sizes[group_sizes >= 2].index

# Filtra solo gruppi con almeno 2 persone
df_filtrato = df[df['Group'].isin(gruppi_validi)].copy()

# Rimuove righe con VIP nullo
df_filtrato = df_filtrato.dropna(subset=['VIP']).copy()

# Verifica se ogni gruppo ha un solo valore valido di VIP
gruppi_unici = (
    df_filtrato.groupby('Group')['VIP']
    .agg(lambda x: x.nunique() == 1)
)

# Mappa risultato su ogni riga
gruppi_unici_dict = gruppi_unici.to_dict()
df_filtrato['Stesso_VIP'] = df_filtrato['Group'].map(gruppi_unici_dict)

# Calcola percentuale
percentuale = df_filtrato['Stesso_VIP'].sum() / len(df_filtrato) * 100
print(round(percentuale, 2))
