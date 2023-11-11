# Geopandas using Python for Data Scientists
Geopandas is a powerful Python library for working with geospatial data, 
allowing data scientists to manipulate, analyze, and visualize geographic 
information. In this comprehensive training program, you will learn the 
fundamentals of Geopandas and how to perform various geospatial data 
analysis tasks.

1. **Installing Geopandas**:
Before we start, make sure you have Geopandas installed. Geopandas relies 
on other geospatial libraries, such as Fiona, Shapely, and PyProj. You can 
install Geopandas along with these dependencies using pip:

```bash 
pip install geopandas
```

To generate a GeoPandas plot of the UK, you'll need a shapefile of the United 
Kingdom to display data and visualise it.

2. **Downloading Shapefile Data:**

Shapefile is a geospatial vector data format for geographic information 
system (GIS) software. It is developed and regulated by Esri.

You can download shapefile data for the UK from various sources. A 
commonly used source is Natural Earth, which provides free vector and 
raster map data. Here's a step-by-step guide:

   - Go to [Natural Earth](https://www.naturalearthdata.com/).
   - Under Downloads, select "Cultural Vectors."
   - Choose the desired scale and download the shapefiles.
   
3. **Python Code for Plotting with GeoPandas:**

Once you've downloaded the shapefile, here's an example of how you could 
plot it using GeoPandas:

```python
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the shapefile data using GeoPandas
file_path = 'path_to_your_downloaded_shapefile.shp'  # Replace with your file path
gdf = gpd.read_file(file_path)

# Plot the map
fig, ax = plt.subplots(figsize=(10, 10))
gdf.plot(ax=ax)
plt.title('Map of the UK')
plt.axis('off')  # Turn off the axis
plt.show()
```

![map_of_the_uk.png](img%2Fmap_of_the_uk.png)

![map_of_the_world.png](img%2Fmap_of_the_world.png)



Replace `'path_to_your_downloaded_shapefile.shp'` with the actual file 
path where you've saved the downloaded shapefile. This code reads the 
shapefile using GeoPandas and plots it using Matplotlib.

Keep in mind that the file path should point to the specific location 
where you saved the shapefile on your system. This code will create a plot 
of the UK using the shapefile's geographical boundaries.

Feel free to modify the plot according to your preferences, such as 
adjusting colors, adding labels, or customizing the plot appearance.

The Shapefile format is much more compact than GeoJSON, and is supported 
by GeoPandas, (Plotly requires GeoJSON, which I created from the Shapefiles later.)

[UK portal of sharp files](https://geoportal.statistics.gov.uk/)

Download Options of Wards (May 2023) [Boundaries UK BFC](https://geoportal.statistics.gov.uk/datasets/ons::wards-may-2023-boundaries-uk-bfc/explore)

[Interactive Mapping in Python with UK Census Data](https://medium.com/@patohara60/interactive-mapping-in-python-with-uk-census-data-6e571c60ff4)