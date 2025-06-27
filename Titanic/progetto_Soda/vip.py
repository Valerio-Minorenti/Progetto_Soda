import pandas as pd

# Caricamento del file
df = pd.read_csv('train.csv')  # Sostituisci con il percorso corretto

# Estrai il gruppo dal PassengerId
df['Group'] = df['PassengerId'].str.split('_').str[0]

# Filtra i passeggeri con VIP nullo
missing_hp = df[df['VIP'].isna()]

# Lista per salvare i risultati
results = []

# Ciclo su ogni passeggero con VIP nullo
for idx, row in missing_hp.iterrows():
    group = row['Group']
    passenger_id = row['PassengerId']
    
    # Trova gli altri membri del gruppo con VIP noto
    group_members = df[(df['Group'] == group) & (df['PassengerId'] != passenger_id) & (df['VIP'].notna())]
    planets = group_members['VIP'].unique().tolist()
    
    results.append({
        'PassengerId': passenger_id,
        'Group': group,
        'OtherGroupVIP': planets
    })
results_df = pd.DataFrame(results)
print(results_df)
##SOLO CHI HA ALMENO UN VALORE T O F
# Carica il file
df = pd.read_csv('train.csv')  # Sostituisci con il percorso corretto

# Estrai il gruppo dal PassengerId
df['Group'] = df['PassengerId'].str.split('_').str[0]

# Filtra i passeggeri con VIP nullo
missing_VIP = df[df['VIP'].isna()]

# Lista per salvare i risultati
VIP_results = []

# Ciclo su ogni passeggero con VIP nullo
for idx, row in missing_VIP.iterrows():
    group = row['Group']
    passenger_id = row['PassengerId']
    
    # Trova altri membri del gruppo con VIP noto
    group_members = df[
        (df['Group'] == group) & 
        (df['PassengerId'] != passenger_id) & 
        (df['VIP'].notna())
    ]
    
    if not group_members.empty:
        sleep_values = group_members['VIP'].unique().tolist()
        VIP_results.append({
            'PassengerId': passenger_id,
            'Group': group,
            'OtherGroupVIPValues': sleep_values
        })

# Converti in DataFrame e mostra
VIP_results_df = pd.DataFrame(VIP_results)
print(VIP_results_df)
###UNO SOLO VALORE UNIFORME
# Carica il file
df = pd.read_csv('train.csv')  # Sostituisci con il percorso corretto

# Estrai il gruppo dal PassengerId
df['Group'] = df['PassengerId'].str.split('_').str[0]

# Filtra i passeggeri con VIP nullo
missing_VIP = df[df['VIP'].isna()]

# Lista per salvare i risultati coerenti
coherent_results = []

# Ciclo su ogni passeggero con VIP nullo
for idx, row in missing_VIP.iterrows():
    group = row['Group']
    passenger_id = row['PassengerId']
    
    # Trova gli altri membri del gruppo con VIP noto
    group_members = df[
        (df['Group'] == group) & 
        (df['PassengerId'] != passenger_id) & 
        (df['VIP'].notna())
    ]
    
    unique_values = group_members['VIP'].unique().tolist()
    
    # Verifica se tutti i valori noti sono uguali (e almeno uno esiste)
    if len(unique_values) == 1:
        coherent_results.append({
            'PassengerId': passenger_id,
            'Group': group,
            'UniformVIPValue': unique_values[0]
        })

# Converti in DataFrame e stampa
coherent_df = pd.DataFrame(coherent_results)
print(coherent_df)
