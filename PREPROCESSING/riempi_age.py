def riempi_age_group(combined_df):
    valore_imputazione = '0-18'  # valore con cui imputare
    before = combined_df['AgeGroup'].isna().sum()
    combined_df['AgeGroup'] = combined_df['AgeGroup'].fillna(valore_imputazione)
    after = combined_df['AgeGroup'].isna().sum()
    print(f"AgeGroup NaN prima: {before}, dopo: {after}")
    
    return combined_df