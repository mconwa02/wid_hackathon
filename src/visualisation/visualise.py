import logging

import geopandas as gpd
import matplotlib.pyplot as plt

from data.raw.local_kaggle_data import creating_uk_hospital_data
from src.visualisation.global_maps import read_world_map


def main():
    logger = logging.getLogger(__name__)
    logger.debug(
        "Creating a DataFrame containing cities with longitudes and"
        " latitudes."
    )
    df = creating_uk_hospital_data()[
        ["City", "County", "Latitude", "Longitude"]
    ]

    logger.debug("Creating a GeoDataFrame from a DataFrame with coordinates")

    gdf = gpd.GeoDataFrame(
        df,
        geometry=gpd.points_from_xy(df.Longitude, df.Latitude),
    )
    print(gdf.head())
    logger.debug(
        f"The max longitude is {df.Longitude.max()} and  min "
        f"longitude is {df.Longitude.min()}"
    )

    world = read_world_map()

    fig, ax = plt.subplots(figsize=(10, 10))
    # world.clip([-10, 45, 5, 70]).plot(ax=ax, color="grey")
    world.clip([-6, 48, 2, 65]).plot(ax=ax, color="grey")
    gdf.plot(ax=ax, color="blue")
    plt.title("NHS Hospitals")
    plt.axis("off")
    plt.show()
    plt.savefig("nhs_hospitals.png")


if __name__ == "__main__":
    main()
