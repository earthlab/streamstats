=====
Usage
=====

Finding the watershed that contains a point
-------------------------------------------

Given a spatial point in the U.S. defined by a lat/lon location and a state,
the `WatershedFinder` class can be used to find the watershed that contains
that point.
First, we define a watershed finder object that can be queried with 
longitude/latitude values.
The `finders.find_watershed` function returns the JSON response from the `USGS
StreamStats API <https://streamstats.usgs.gov/docs/streamstatsservices/>`_.

    from streamstats import finders

    res = finders.find_watershed(lon=-74.524, lat=43.939)
