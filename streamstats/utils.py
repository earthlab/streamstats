# -*- coding: utf-8 -*-
"""Utility functions for streamstats."""

import geopy


def find_address(lat, lon):
    """Find the address associated with a lat/lon pair.
    :param lat: Latitude of point in decimal degrees
    :type lat: float
    :param lon: Longitude of point in decimal degrees
    :type lon: float
    :rtype: dictionary containing address data
    """
    locator = geopy.geocoders.Nominatim(user_agent='streamstats')
    location_info = locator.reverse(", ".join([str(lat), str(lon)]))
    no_result_found = location_info[0] is None
    if no_result_found:
        raise ValueError('No results found!')  # make this better
    address = location_info.raw['address']
    assert address['country'] == 'USA', 'Point must be in US (50 states)'
    return address


def find_state(address):
    """Find the U.S. state that contains an address

    :param address: An address found by ``find_address``
    :type address: dict
    :rtype: string of the state code (e.g., "CO" for Colorado)
    """
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
    'District Of Columbia': 'DC',
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
    'Wyoming': 'WY'
}
