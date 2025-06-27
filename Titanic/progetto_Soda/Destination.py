import pandas as pd

# Caricamento del file
df = pd.read_csv('train.csv')  # Sostituisci con il percorso corretto

# Estrai il gruppo dal PassengerId
df['Group'] = df['PassengerId'].str.split('_').str[0]

# Filtra i passeggeri con Destination nullo
missing_hp = df[df['Destination'].isna()]

# Lista per salvare i risultati
results = []

# Ciclo su ogni passeggero con Destination nullo
for idx, row in missing_hp.iterrows():
    group = row['Group']
    passenger_id = row['PassengerId']
    
    # Trova gli altri membri del gruppo con Destination noto
    group_members = df[(df['Group'] == group) & (df['PassengerId'] != passenger_id) & (df['Destination'].notna())]
    planets = group_members['Destination'].unique().tolist()
    
    results.append({
        'PassengerId': passenger_id,
        'Group': group,
        'OtherGroupDestination': planets
    })
results_df = pd.DataFrame(results)
print(results_df)
##SOLO CHI HA ALMENO UN VALORE T O F
# Carica il file
df = pd.read_csv('train.csv')  # Sostituisci con il percorso corretto

# Estrai il gruppo dal PassengerId
df['Group'] = df['PassengerId'].str.split('_').str[0]

# Filtra i passeggeri con Destination nullo
missing_Destination = df[df['Destination'].isna()]

# Lista per salvare i risultati
Destination_results = []

# Ciclo su ogni passeggero con Destination nullo
for idx, row in missing_Destination.iterrows():
    group = row['Group']
    passenger_id = row['PassengerId']
    
    # Trova altri membri del gruppo con Destination noto
    group_members = df[
        (df['Group'] == group) & 
        (df['PassengerId'] != passenger_id) & 
        (df['Destination'].notna())
    ]
    
    if not group_members.empty:
        sleep_values = group_members['Destination'].unique().tolist()
        Destination_results.append({
            'PassengerId': passenger_id,
            'Group': group,
            'OtherGroupDestinationValues': sleep_values
        })

# Converti in DataFrame e mostra
Destination_results_df = pd.DataFrame(Destination_results)
print(Destination_results_df)
###UNO SOLO VALORE UNIFORME
# Carica il file
df = pd.read_csv('train.csv')  # Sostituisci con il percorso corretto

# Estrai il gruppo dal PassengerId
df['Group'] = df['PassengerId'].str.split('_').str[0]

# Filtra i passeggeri con Destination nullo
missing_Destination = df[df['Destination'].isna()]

# Lista per salvare i risultati coerenti
coherent_results = []

# Ciclo su ogni passeggero con Destination nullo
for idx, row in missing_Destination.iterrows():
    group = row['Group']
    passenger_id = row['PassengerId']
    
    # Trova gli altri membri del gruppo con Destination noto
    group_members = df[
        (df['Group'] == group) & 
        (df['PassengerId'] != passenger_id) & 
        (df['Destination'].notna())
    ]
    
    unique_values = group_members['Destination'].unique().tolist()
    
    # Verifica se tutti i valori noti sono uguali (e almeno uno esiste)
    if len(unique_values) == 1:
        coherent_results.append({
            'PassengerId': passenger_id,
            'Group': group,
            'UniformDestinationValue': unique_values[0]
        })

# Converti in DataFrame e stampa
coherent_df = pd.DataFrame(coherent_results)
print(coherent_df)
