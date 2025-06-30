# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 10:43:53 2025

@author: matmi
"""
import pandas as pd

# Caricamento del dataset
df = pd.read_csv("C:/Users/matmi/Desktop/cartella Versionata PROGETTO SODA/Titanic/train.csv")

# Estrai Deck, CabinNum e Side dalla colonna Cabin
df[['Deck', 'CabinNum', 'Side']] = df['Cabin'].str.split('/', expand=True)

# Copia per encoding
df_encoded = df.copy()

# Colonne categoriche da codificare
categorical_cols = ['HomePlanet', 'CryoSleep', 'Cabin', 'Destination', 'VIP', 'Deck', 'Side']
for col in categorical_cols:
    df_encoded[col] = df_encoded[col].astype('category').cat.codes

# Codifica del target
df_encoded['Transported'] = df_encoded['Transported'].astype('category').cat.codes

# Rimuovi colonne Name e PassengerId
df_encoded = df_encoded.drop(columns=['Name', 'PassengerId'])

# Calcola la correlazione
correlation_matrix = df_encoded.corr()
target_corr = correlation_matrix['Transported'].drop('Transported').sort_values(key=abs, ascending=False)

# Stampa i risultati
for feature, corr in target_corr.items():
    print(f"{feature}: correlazione {corr:.2f}")
