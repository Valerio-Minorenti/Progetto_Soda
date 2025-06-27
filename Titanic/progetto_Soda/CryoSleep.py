import pandas as pd
##SOLO CHI HA ALMENO UN VALORE T O F
# Carica il file
df = pd.read_csv('train.csv')  # Sostituisci con il percorso corretto

# Estrai il gruppo dal PassengerId
df['Group'] = df['PassengerId'].str.split('_').str[0]

# Filtra i passeggeri con CryoSleep nullo
missing_cryosleep = df[df['CryoSleep'].isna()]

# Lista per salvare i risultati
cryosleep_results = []

# Ciclo su ogni passeggero con CryoSleep nullo
for idx, row in missing_cryosleep.iterrows():
    group = row['Group']
    passenger_id = row['PassengerId']
    
    # Trova altri membri del gruppo con CryoSleep noto
    group_members = df[
        (df['Group'] == group) & 
        (df['PassengerId'] != passenger_id) & 
        (df['CryoSleep'].notna())
    ]
    
    if not group_members.empty:
        sleep_values = group_members['CryoSleep'].unique().tolist()
        cryosleep_results.append({
            'PassengerId': passenger_id,
            'Group': group,
            'OtherGroupCryoSleepValues': sleep_values
        })

# Converti in DataFrame e mostra
cryosleep_results_df = pd.DataFrame(cryosleep_results)
print(cryosleep_results_df)

####TUTTI I  VALORI NULLI
import pandas as pd

# Carica il file
df = pd.read_csv('train.csv')  # Sostituisci con il percorso corretto

# Estrai il gruppo dal PassengerId
df['Group'] = df['PassengerId'].str.split('_').str[0]

# Filtra i passeggeri con CryoSleep nullo
missing_cryosleep = df[df['CryoSleep'].isna()]

# Lista per salvare i risultati
cryosleep_results = []

# Ciclo su ogni passeggero con CryoSleep nullo
for idx, row in missing_cryosleep.iterrows():
    group = row['Group']
    passenger_id = row['PassengerId']
    
    # Trova altri membri del gruppo con valore noto in CryoSleep
    group_members = df[
        (df['Group'] == group) & 
        (df['PassengerId'] != passenger_id) & 
        (df['CryoSleep'].notna())
    ]
    
    sleep_values = group_members['CryoSleep'].unique().tolist()
    
    cryosleep_results.append({
        'PassengerId': passenger_id,
        'Group': group,
        'OtherGroupCryoSleepValues': sleep_values
    })

# Converti in DataFrame e mostra
cryosleep_results_df = pd.DataFrame(cryosleep_results)
print(cryosleep_results_df)
import pandas as pd
###UNO SOLO VALORE UNIFORME
# Carica il file
df = pd.read_csv('train.csv')  # Sostituisci con il percorso corretto

# Estrai il gruppo dal PassengerId
df['Group'] = df['PassengerId'].str.split('_').str[0]

# Filtra i passeggeri con CryoSleep nullo
missing_cryosleep = df[df['CryoSleep'].isna()]

# Lista per salvare i risultati coerenti
coherent_results = []

# Ciclo su ogni passeggero con CryoSleep nullo
for idx, row in missing_cryosleep.iterrows():
    group = row['Group']
    passenger_id = row['PassengerId']
    
    # Trova gli altri membri del gruppo con CryoSleep noto
    group_members = df[
        (df['Group'] == group) & 
        (df['PassengerId'] != passenger_id) & 
        (df['CryoSleep'].notna())
    ]
    
    unique_values = group_members['CryoSleep'].unique().tolist()
    
    # Verifica se tutti i valori noti sono uguali (e almeno uno esiste)
    if len(unique_values) == 1:
        coherent_results.append({
            'PassengerId': passenger_id,
            'Group': group,
            'UniformCryoSleepValue': unique_values[0]
        })

# Converti in DataFrame e stampa
coherent_df = pd.DataFrame(coherent_results)
print(coherent_df)
