from pathlib import Path

import pandas as pd

from src.data.config import DATA_PATH

uk_nhs_hospital_database = pd.read_csv(Path(DATA_PATH, "Hospital.csv"))

df = uk_nhs_hospital_database
print(df.head())
print(df.columns)
print(df.describe())
print(df.info())
print(
    f"There is the following {df.City.nunique()} city "
    f"locations in the feature {df.City.value_counts()}"
)
