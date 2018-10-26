# -*- coding: utf-8 -*-
"""Functionality for finding watershed information for specific locations."""

import requests
import geopy
import streamstats


def find_watershed(lon, lat):
    """Find the watershed that contains a point

    :param lon: Longitude of point in decimal degrees.
    :type lon: float
    :param lat: Latitude of point in decimal degrees.
    :type lat: float
    :rtype: dict containing watershed data
    """
    baseurl = "".join([streamstats.BASE_URL, "watershed.geojson"])
    payload = {
        'rcode': find_state(lon, lat),
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


def find_state(lon, lat):
    """Find the U.S. state that contains a point

    :param lon: Longitude of point in decimal degrees
    :type lon: float
    :param lat: Latitude of point in decimal degrees
    :type lat: float
    :rtype: string of the state code (e.g., CO for Colorado)
    """
    state_locator = geopy.geocoders.Nominatim(user_agent='streamstats')
    location_info = state_locator.reverse(", ".join([str(lat), str(lon)]))
    address = location_info.raw['address']
    assert address['country'] == 'USA', 'Point must be in U.S.'
    state_code = US_STATE_ABBREV[address['state']]
    return state_code


US_STATE_ABBREV = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
