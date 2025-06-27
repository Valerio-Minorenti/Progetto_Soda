import pandas as pd

# Caricamento del file
df = pd.read_csv('train.csv')  # Sostituisci con il percorso corretto

# Estrai il gruppo dal PassengerId
df['Group'] = df['PassengerId'].str.split('_').str[0]

# Conta le dimensioni dei gruppi
group_sizes = df['Group'].value_counts()

# Filtra i passeggeri con HomePlanet nullo
missing_hp = df[df['HomePlanet'].isna()]

# Lista per salvare i risultati
results = []

# Ciclo su ogni passeggero con HomePlanet nullo
for idx, row in missing_hp.iterrows():
    group = row['Group']
    passenger_id = row['PassengerId']
    
    # Verifica che il gruppo abbia almeno 2 persone
    if group_sizes[group] < 2:
        continue

    # Trova altri membri del gruppo con HomePlanet noto
    group_members = df[
        (df['Group'] == group) &
        (df['PassengerId'] != passenger_id) &
        (df['HomePlanet'].notna())
    ]
    
    if not group_members.empty:
        planets = group_members['HomePlanet'].unique().tolist()
        results.append({
            'PassengerId': passenger_id,
            'Group': group,
            'OtherGroupHomePlanets': planets
        })

# Converti in DataFrame e mostra
results_df = pd.DataFrame(results)
print(results_df)
