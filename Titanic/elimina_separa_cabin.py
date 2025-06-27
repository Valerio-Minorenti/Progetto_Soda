import pandas as pd

# Legge il file Excel
df = pd.read_excel("trainozzo.xlsx")

# Estrae il gruppo da PassengerId
df['Group'] = df['PassengerId'].str.split('_').str[0]

# Estrae le 3 componenti dalla colonna Cabin
df[['Deck', 'Num', 'Side']] = df['Cabin'].str.split('/', expand=True)

# Droppa la colonna Cabin
df.drop(columns=['Cabin'], inplace=True)

# Salva il nuovo file Excel
df.to_excel("train_cabin.xlsx", index=False)
