from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt

from src.data.config import DATA_PATH


def read_uk_map():
    # Get UK Boundaries as GeoPandas
    shapefile = Path(DATA_PATH, "WD_MAY_2023_UK_BFC.shp")
    gdf = gpd.read_file(shapefile)
    return gdf


def read_world_map():
    # Load the shapefile data using GeoPandas
    shapefile = Path(DATA_PATH, "ne_10m_admin_0_sovereignty.shp")
    # Replace with your file path
    gdf = gpd.read_file(shapefile)
    return gdf


def plot_geopandas_map(gdf, title):
    fig, ax = plt.subplots(figsize=(10, 10))
    gdf.plot(ax=ax)
    plt.title(title)
    plt.axis("off")
    plt.show()


uk_gdf = read_uk_map()
world_gdf = read_world_map()

plot_geopandas_map(uk_gdf, "Map of the UK")
plot_geopandas_map(world_gdf, "Map of the World")
