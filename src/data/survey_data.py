import os

import pandas as pd
from sklearn.preprocessing import LabelEncoder

DIR_PATH = r"C:\dev\data\wid_hack\survey_data"

# original survey data with weights
df = pd.read_csv(
    os.path.join(DIR_PATH, "Final Output v2 with weights.csv"),
    low_memory=True,
)

# reading writing to parquet for faster read ins
df.to_parquet(r"C:\dev\data\wid_hack\survey_data\final.pq")
df = pd.read_parquet(os.path.join(DIR_PATH, "final.pq"))

# data dictionary of all unique values on each columns
# todo create a markdown data dictionary of cleaned values
dict_df = pd.DataFrame()
for col in df.columns:
    dict_df[col] = pd.Series(df[col].unique())
    print(f"column \n{col}: \n{df[col].unique()}")
dict_df.to_csv(os.path.join(DIR_PATH, "unique_values.csv"), index=False)

# two surveys were merged replacing full stop to reduce duplicates
# todo fix bug
df = df.replace(".", "")

# merging region into 1 column as a categorical feature - demog_constituency
df["demog_constituency"] = (
    df["demog_region_ee"]
    + df["demog_region_em"]
    + df["demog_region_lon"]
    + df["demog_region_ne"]
    + df["demog_region_nw"]
    + df["demog_region_ni"]
    + df["demog_region_scot"]
    + df["demog_region_se"]
    + df["demog_region_sw"]
    + df["demog_region_wales"]
    + df["demog_region_wm"]
    + df["demog_region_york"]
)

keep_cols = [
    "id",
    "demog_age",
    "demog_gender",
    "demog_ethnicity",
    "demog_social_grade",
    "demog_region",
    "demog_constituency",
]


# Convert categorical data to numerical data using LabelEncoder
le = LabelEncoder()
# Using data from columns 33 onwards as after constituency
for col in df.iloc[:, 33:].columns:
    # Tidy null values and duplicates
    df[col] = df[col].replace("Prefer not to say", None)
    df[col] = df[col].replace("Not asked", None)
    df[col] = df[col].replace("Not asked", None)
    df[col] = df[col].replace(".", "")
    # todo replace optional I dont know - None
    if df[col].nunique() <= 1:
        df[col] = le.fit_transform(df[col])
    if df[col].nunique() > 3:
        # todo need to check what can be converted to numerical
        print("******** values greater than 3 **********")
        print(col)

cleaned_df = pd.concat([df[keep_cols], df.iloc[:, 33:]], axis=1)
data_dict_df = pd.concat([df.iloc[:, :33], df.iloc[:, 33:]], axis=1)
data_dict_df.to_csv(
    os.path.join(DIR_PATH, "data_dictionary.csv"), index=False
)
cleaned_df.to_csv(os.path.join(DIR_PATH, "cleaned_data.csv"), index=False)
