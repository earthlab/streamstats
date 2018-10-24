# -*- coding: utf-8 -*-
"""Functionality for finding watershed information for specific locations."""

import requests
import streamstats


def find_watershed(state, lon, lat):
    """Find the watershed that contains a point

    :param state: Two character state code, e.g. "CA" for California.
    :type state: string
    :param lon: Longitude of point in decimal degrees.
    :type lon: float
    :param lat: Latitude of point in decimal degrees.
    :type lat: float
    :rtype: dict containing watershed data
    """
    baseurl = "".join([streamstats.BASE_URL, "watershed.geojson"])
    payload = {
        'rcode': state,
        'xlocation': lon,
        'ylocation': lat,
        'crs': 4326,
        'includeparameters': True,
        'includeflowtypes': False,
        'includefeatures': True,
        'simplify': False
    }
    response = requests.get(baseurl, params=payload)
    response.raise_for_status()  # raises errors early
    return response.json()
