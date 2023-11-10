import geopandas as gpd
import geodatasets
import matplotlib.pyplot as plt

df = gpd.read_file(geodatasets.get_path("nybb"))
ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor="k")
plt.show()
