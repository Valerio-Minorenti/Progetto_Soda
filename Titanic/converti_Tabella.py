import pandas as pd

# Percorso del file CSV
csv_file = 'C:/Users/Standard/Desktop/Titanic/progetto_Soda/train.csv'

# Percorso del file Excel di output
excel_file = 'C:/Users/Standard/Desktop/Titanic/progetto_Soda/trainozzo.xlsx'

# Leggi il file CSV
df = pd.read_csv(csv_file)

# Salva il file in formato Excel
df.to_excel(excel_file, index=False)

print(f"Conversione completata: '{csv_file}' → '{excel_file}'")
