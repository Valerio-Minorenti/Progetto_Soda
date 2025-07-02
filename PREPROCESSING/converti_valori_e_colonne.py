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
df[['Deck', 'CabinNum', 'Side']] = df['Cabin'].str.split('/', expand=True)

# Droppa la colonna Cabin
df.drop(columns=['Cabin'], inplace=True)


# Estrae il cognome dalla colonna Name
df['Surname'] = df['Name'].str.split().str[-1]

# Droppa la colonna Name
df.drop(columns=['Name'], inplace=True)

# Salva il file finale
df.to_excel(output_file, index=False)
print(f"File finale salvato in: '{output_file}'")


deck_counts = Counter(data['Deck'].dropna())
for idx in data[solo & data['Deck'].isna()].index:
    min_count = min(deck_counts.values())
    least_used_decks = [deck for deck, count in deck_counts.items() if count == min_count]
    chosen_deck = least_used_decks[0]
    data.at[idx, 'Deck'] = chosen_deck
    deck_counts[chosen_deck] += 1

# Assegna Side mancante in base a Transported
for idx in data[solo & data['Side'].isna()].index:
    transported = data.at[idx, 'Transported']
    if transported is True:
        data.at[idx, 'Side'] = 'S'
    elif transported is False:
        data.at[idx, 'Side'] = 'P'

# Controlla quanti valori mancanti restano
missing_deck = data.loc[solo, 'Deck'].isna().sum()
missing_cabin_number = data.loc[solo, 'Number'].isna().sum()
missing_side = data.loc[solo, 'Side'].isna().sum()
print(f"Valori mancanti in Deck: {missing_deck}")
print(f"Valori mancanti in CabinNumber: {missing_cabin_number}")
print(f"Valori mancanti in Side: {missing_side}")
