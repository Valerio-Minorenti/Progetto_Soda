import pandas as pd

# Carica il CSV
df = pd.read_csv("train.csv")

# Estrai il cognome e il gruppo
df['Surname'] = df['Name'].str.split().str[-1]
df['Group'] = df['PassengerId'].str.split('_').str[0]

# Filtra righe valide
df_valid = df.dropna(subset=['Surname', 'Group', 'CryoSleep'])

# Inizializza contatori
total_families_same_group = 0
same_cryosleep_families = 0
total_cryosleep_true_members = 0
coherent_families_all_false = 0

# Analisi per famiglia+gruppo
for (surname, group), group_df in df_valid.groupby(['Surname', 'Group']):
    if len(group_df) >= 2:
        total_families_same_group += 1
        if group_df['CryoSleep'].nunique() == 1:
            same_cryosleep_families += 1
            if group_df['CryoSleep'].iloc[0] == True:
                total_cryosleep_true_members += len(group_df)
            else:  # Tutti False
                coherent_families_all_false += 1

# Percentuale
if total_families_same_group > 0:
    percentage = (same_cryosleep_families / total_families_same_group) * 100
else:
    percentage = 0

# Risultati
print(f"Numero totale di famiglie nello stesso gruppo (almeno 2 persone): {total_families_same_group}")
print(f"Numero di famiglie con stato CryoSleep uguale per tutti i membri: {same_cryosleep_families}")
print(f"Percentuale di famiglie con CryoSleep coerente: {percentage:.2f}%")
print(f"Totale persone in CryoSleep = True all'interno di famiglie coerenti: {total_cryosleep_true_members}")
print(f"Numero di famiglie coerenti con tutti i membri in CryoSleep = False: {coherent_families_all_false}")
