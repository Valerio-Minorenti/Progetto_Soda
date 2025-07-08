from riempi_Home_Planet import riempi_Home_Planet
from riempi_VIP import riempi_vip
from riempi_cryo import riempi_cryo
from riempi_deck import riempi_deck
from riempi_Destination import riempi_Destination
from riempi_Surname import riempi_Surname
from riempi_side import riempi_side
from missing_values import missing_values
from encoding import encoding_statico
from adaboost import adaboost
from riempi_age import riempi_age_group
from riempi_cabinregion import riempi_cabinregion
from RandomForest import train_random_forest

def imputazione(combined_df, target_column='Transported'):
    combined_df = riempi_Home_Planet(combined_df)
    combined_df = riempi_vip(combined_df)
    combined_df = riempi_cryo(combined_df)
    combined_df = riempi_deck(combined_df)
    combined_df = riempi_side(combined_df)
    combined_df = riempi_cabinregion(combined_df)
    combined_df = riempi_Surname(combined_df)
    combined_df = riempi_Destination(combined_df)
    combined_df = riempi_age_group(combined_df)
    combined_df = missing_values(combined_df)
    df_train_encoded, df_val_encoded, df_test_encoded = encoding_statico(combined_df)
    ad_model = adaboost(df_train_encoded, df_val_encoded, target_column, n_estimators=100, random_state=42)
    rf_model = train_random_forest(df_train_encoded, df_val_encoded, target_column)
    return combined_df, ad_model, rf_model #, df_train_encoded, df_val_encoded, df_test_encoded, perché non li ritorniamo?