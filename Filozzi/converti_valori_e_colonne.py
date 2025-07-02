import pandas as pd

# Percorso del file CSV
csv_file = 'C:/Users/Standard/Desktop/Titanic/progetto_Soda/train.csv'

# Percorso intermedio Excel
excel_file = 'C:/Users/Standard/Desktop/Titanic/progetto_Soda/trainozzo.xlsx'

# Percorso finale
output_file = 'tabellozza.xlsx'

# Legge il file CSV
df = pd.read_csv(csv_file)

# Salva il file in formato Excel
df.to_excel(excel_file, index=False)
print(f"Conversione completata: '{csv_file}' → '{excel_file}'")

# Riapre il file Excel
df = pd.read_excel(excel_file)

# Estrae il gruppo da PassengerId
df['Group'] = df['PassengerId'].str.split('_').str[0]

# Estrae le componenti della Cabina
df[['Deck', 'Num', 'Side']] = df['Cabin'].str.split('/', expand=True)

# Droppa la colonna Cabin
df.drop(columns=['Cabin'], inplace=True)


# Estrae il cognome dalla colonna Name
df['Surname'] = df['Name'].str.split().str[-1]

# Droppa la colonna Name
df.drop(columns=['Name'], inplace=True)

# Salva il file finale
df.to_excel(output_file, index=False)
print(f"File finale salvato in: '{output_file}'")
