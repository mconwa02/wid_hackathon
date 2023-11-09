from pathlib import Path

import pandas as pd

from data.config import DATA_PATH

uk_nhs_hospital_database = pd.read_csv(Path(DATA_PATH, "Hospital.csv"))
print(uk_nhs_hospital_database.head())
