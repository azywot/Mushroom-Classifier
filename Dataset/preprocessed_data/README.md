# Preprocessed data

File fraud_oracle_preprocessed.csv is data in which I remove one row which has empty two values (as the only one) and in rows where column Age was empty values are imputed using k-nn with 10 neighbors

File fraud_oracle_preprocessed_drop.csv is fraud_oracle_preprocessed.csv after drop two columns: PolicyNumber (ID), PolicyType (VehicleCategory + BasePolicy)