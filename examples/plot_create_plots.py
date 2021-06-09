"""
Download Data with StreamStats
===============================================================

Learn how to use StreamStats python library to download watershed boundary data
available in USGS StreamStats API. StreamStats provides information including
HUC code, a GeoJSON representation of the polygon associated with the watershed,
and basin characteristics.
"""

###########################################################################
# Import Packages
# -------------------------------------------------------
# Download the necessary Python packages. The ``GeoPandas`` package is an open
# source project that assists in working with geospatial data in Python. Learn
# more about `GeoPandas <https://geopandas.org/index.html>`_.

import streamstats
import geopandas as gpd

###########################################################################
# Identify watershed
# ---------------------
# To identify a HUC, use a latitude and longitude value to select a specific watershed.
# Assign cordinates to variables ``lat`` and ``lon``. Using StreamStat's data,
# assign location to a variable that will represent the
# delineated watershed using the USGS StreamStats API.

lat, lon = 39.966256, -105.482227
ws = streamstats.Watershed(lat=lat, lon=lon)

###########################################################################
# Find boundary properties of the watershed
# ------------------------------------------
# ``ws.boundary`` is a stored variable in the watershed object and will return
# the full watershed GeoJSON as a dictionary. You can access the CRS through
# the GeoJSON object.

ws.boundary
ws.boundary['crs']

###########################################################################
# Create plot of the Watershed
# -----------------------------
# Open the GeoJSON with GeoPandas and plot the data.

ws.boundary
poly = gpd.GeoDataFrame.from_features(ws.boundary["features"], crs="EPSG:4326")
ax = poly.plot(figsize=(20, 10), edgecolor='k')
ax.set_title("Single Watershed", fontsize=30, fontweight = 'bold')
ax.set_axis_off()
