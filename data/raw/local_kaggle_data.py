from pathlib import Path

import pandas as pd

from src.data.config import DATA_PATH


def creating_uk_hospital_data():
    df = pd.read_csv(Path(DATA_PATH, "Hospital.csv"))
    print(df.head())
    print(df.columns)
    print(df.describe())
    print(df.info())
    print(
        f"There is the following {df.City.nunique()} city "
        f"locations in the feature {df.City.value_counts()}"
    )
    return df


if __name__ == "__main__":
    creating_uk_hospital_data()
