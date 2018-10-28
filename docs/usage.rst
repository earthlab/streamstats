=====
Usage
=====

Finding the watershed that contains a point
-------------------------------------------

Given a spatial point in the U.S. defined by a lat/lon location and a state,
the `Watershed` class can be used to find the watershed that contains
that point using the `USGS
StreamStats API <https://streamstats.usgs.gov/docs/streamstatsservices/>`_.

    >>> from streamstats import Watershed
    >>> Watershed(lat=43.939, lon=-74.524)
    Watershed object with HUC8: 04150305, containing lat/lon: (43.939, -74.524)
