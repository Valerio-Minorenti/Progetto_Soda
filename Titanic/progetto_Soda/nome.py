import pandas as pd

# Carica il file CSV
df = pd.read_csv('train.csv')  # Sostituisci con il percorso corretto del tuo file

# Estrai il cognome (seconda parola nella colonna Name)
df['Surname'] = df['Name'].str.split().str[1]

# Raggruppa per cognome e analizza la colonna Transported
results = []
for surname, group in df.groupby('Surname'):
    total_people = len(group)
    unique_transported = group['Transported'].dropna().unique()
    
    # Aggiungi solo se tutti hanno lo stesso valore (True o False)
    if len(unique_transported) == 1:
        results.append({
            'Surname': surname,
            'TotalPeople': total_people,
            'SameTransportedValue': unique_transported[0]
        })

# Converte in DataFrame e stampa
consistent_df = pd.DataFrame(results)
print(consistent_df)
