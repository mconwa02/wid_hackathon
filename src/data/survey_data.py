import os

import pandas as pd
from sklearn.preprocessing import LabelEncoder

DIR_PATH = r"C:\dev\data\wid_hack\survey_data"

# # original survey data with weights
# df = pd.read_csv(
#     os.path.join(DIR_PATH, "Final Output v2 with weights.csv"),
#     low_memory=True,
# )
#
# # reading writing to parquet for faster read ins
# df.to_parquet(r"C:\dev\data\wid_hack\survey_data\final.pq")
df = pd.read_parquet(os.path.join(DIR_PATH, "final.pq"))


def replace_remove_values(df):
    """two surveys were merged replacing full stop to reduce duplicates"""
    df = df.replace("Prefer not to say", None)
    df = df.replace("Not asked", None)
    df = df.replace("No, I did not report", None)
    df = df.replace(
        "Vehicle crime e.g. damage to your car or vehicle",
        "Damage to your car or vehicle",
    )
    df = df.replace(
        "Being physically followed, pestered or chased.",
        "Being physically followed, pestered or chased",
    )
    df = df.replace(
        "Being forced against your will to participate in sexual behaviour",
        "Being forced against your will into participating into sexual behaviour",
    )
    df = df.replace(
        "Online comments or jokes of a sexual nature about you or others that made you feel uncomfortable."
        "Online comments or jokes of a sexual nature about you or others that made you feel uncomfortable",
    )
    df = df.replace(
        "Catcalls, whistles or other provocative sounds which made you feel uncomfortable.",
        "Catcalls, whistles or other provocative sounds which made you feel uncomfortable",
    )
    df = df.replace(
        "Unwanted sexual comments or jokes from someone you know about your body and / or clothes which made you feel uncomfortable.",
        "Unwanted sexual comments or jokes from someone you know about your body and / or clothes which made you feel uncomfortable",
    )
    df = df.replace(
        "Coercive control - a pattern of behaviour over time to exert power and " "control, blaming you for the abuse or ‚Äògas-lighting‚Äô you.",
        "Coercive control - a pattern of behaviour over time to exert power and control, blaming you for the abuse or ‚Äògas-lighting‚Äô you"
    )

    df = df.replace(
        "Donâ€šÃ„Ã´t know, havenâ€šÃ„Ã´t decided yet"
        "Don't know, haven't decided yet"
    )
    return df


df = replace_remove_values(df)

for col in df.columns:
    if df[col].nunique() == 2:
        print(f"**** ---- column {col}: has {df[col].nunique()} unique values")

# data dictionary of all unique values on each columns
dict_df = pd.DataFrame()
for col in df.columns:
    dict_df[col] = pd.Series(df[col].unique())
    print(f"column {col}: has {df[col].nunique()} unique values")
dict_df.to_csv(os.path.join(DIR_PATH, "unique_values.csv"), index=False)


# # open text columns really good for natu
# # df['reportedoutcome_public_other']
# # df['nonreportreason_public_other']
# # df['reportedoutcome_online_other']
# # df['nonreportreason_online_other']
# # df['reportedoutcome_private_other']
# # df['nonreportreason_private_other']
# # df['safeactions_other']
# # df['demog_health_somethingelse']
# # df['optionalreporting_other']
#
# # todo merge
# # considercrime_public_forcesex
# # considercrime_public_rape

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
    if df[col].nunique() <= 1:
        df[col] = le.fit_transform(df[col])
    if df[col].nunique() > 3:
        print("******** values greater than 3 **********")
        print(f"column \n{col}: has \n{df[col].nunique()} unique values")

cleaned_df = pd.concat([df[keep_cols], df.iloc[:, 33:]], axis=1)
cleaned_df.to_csv(os.path.join(DIR_PATH, "cleaned_data.csv"), index=False)

# data_dict_df = pd.concat([df.iloc[:, :33], df.iloc[:, 33:]], axis=1)
# data_dict_df.to_csv(
#     os.path.join(DIR_PATH, "data_dictionary.csv"), index=False
# )
