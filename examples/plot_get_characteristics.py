"""
View Watershed Characterisitics Using StreamStats
===============================================================
"""
###########################################################################
# Import Packages
# ----------------
# To get started, download the necessary Python packages. The``GeoPandas``
# package is an open source project that assists in working with geospatial data
# in Python. Learn more about
# 'GeoPandas<https://geopandas.org/gallery/index.html>'_.

import streamstats
import geopandas as gpd

###########################################################################
# Indentify watershed
# ---------------------
# Identify a spatial point using coordinate system (e.g., longitude and latitude
# cordinates). Assign cordinates to variables ``lat`` and ``lon``. Using
# StreamStat's data, assign location to a variable that will represent the
# delineated watershed using the USGS StreamStats API.

lat, lon = 39.966256, -105.482227
ws = streamstats.Watershed(lat=lat, lon=lon)

###########################################################################
# Find the Hydrologic Unit Code (HUC) of the watershed
# -----------------------------------------------------
# The USGS delineates watershed using a series of numbers based a hierarchal
# region system. Every watershed is assigned a series of numbers called the
# hydrological unit code (HUC). StreamStats uses HUC to identify and delineate
# watersheds. The ``ws.huc`` function will return the HUC of the identified
# watershed.

ws.huc

###########################################################################
# Find Characteristics of the watershed
# --------------------------------------
# The function ``ws.characteristics`` will return the available basin
# characteristics for the identified watershed.In order to return information
# on a specific characteristic, use function
# ``ws.get_characteristic('StatLabel')``.

# 'Learn more<https://streamstatsags.cr.usgs.gov/ss_defs/basin_char_defs.aspx>'_
# about StreamStats Basin Characteristic Definitions.

# Available characteristics
ws.characteristics

# Specific characteristics
ws.get_characteristic('DRNAREA')
