=====
Usage
=====

Finding the watershed that contains a point
-------------------------------------------

Given a spatial point in the U.S. defined by a lat/lon location and a state,
the `WatershedFinder` class can be used to find the watershed that contains
that point.
First, we define a watershed finder object that can be queried with a two
character state code, and longitude/latitude values.
The `WatershedFinder.query` method returns the response from the `USGS
StreamStats API <https://streamstats.usgs.gov/docs/streamstatsservices/>`_.
This response can be converted into JSON by calling the `.json()` method::

    from streamstats import finders

    f = finders.WatershedFinder()
    res = f.query(state='NY', lon=-74.524, lat=43.939)
    res_json = res.json()
