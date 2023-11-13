import logging
from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt

from data.raw.local_kaggle_data import creating_uk_hospital_data


def main():
    """Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info("making final data set from raw data")
    raw_df = creating_uk_hospital_data()

    logger.info(
        "Creating a DataFrame containing cities with longitudes and"
        " latitudes."
    )
    df = raw_df[["City", "County", "Latitude", "Longitude"]]

    logger.info("Creating a GeoDataFrame from a DataFrame with coordinates")
    logger.info(
        "A GeoDataFrame needs a shapely object to transform "
        "Longitude and Latitude into a list of shapely"
    )

    gdf = gpd.GeoDataFrame(
        df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude)
    )
    print(gdf.head())

    fig, ax = plt.subplots(figsize=(24, 18))
    gdf.plot(ax=ax, color="red", legend=True)
    plt.title("NHS Hospitals")
    plt.show()

    return df


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    main()
