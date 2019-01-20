# -*- coding: utf-8 -*-
"""Functionality for finding watershed information for specific locations."""

from collections import OrderedDict
from streamstats import utils


class Watershed():
    """Watershed covering a spatial region, with associated information.

    The USGS StreamStats API is built around watersheds as organizational
    units. Watersheds in the 50 U.S. states can be found using lat/lon
    lookups, along with information about the watershed including its HUC code
    and a GeoJSON representation of the polygon of a watershed. Basin
    characteristics can also be extracted from watersheds.
    """
    base_url = "https://streamstats.usgs.gov/streamstatsservices/"

    def __init__(self, lat, lon):
        """Initialize a Watershed object

        :param lon: Longitude of point in decimal degrees.
        :type lon: float
        :param lat: Latitude of point in decimal degrees.
        :type lat: float
        :param simplify: Whether to simplify the polygon representation.
        :type simplify: bool
        """
        self.lat, self.lon = lat, lon
        self.state = utils.find_state(utils.find_address(lat=lat, lon=lon))
        self.data = self._delineate()
        self.workspace = self.data['workspaceID']
        self.parameters = self.data['parameters']

    def __repr__(self):
        """Get the string representation of a watershed."""
        huc = self.get_huc()
        huc_message = 'Watershed object with HUC%s: %s' % (len(huc), huc)
        coord_message = 'containing lat/lon: (%s, %s)' % (self.lat, self.lon)
        return ', '.join((huc_message, coord_message))

    def _delineate(self):
        """Find the watershed that contains a point.

        Implements a Delineate Watershed by Location query from
        https://streamstats.usgs.gov/docs/streamstatsservices/#/

        :rtype dict containing watershed data
        """
        payload = {
            'rcode': self.state,
            'xlocation': self.lon,
            'ylocation': self.lat,
            'crs': 4326,
            'includeparameters': True,
            'includeflowtypes': False,
            'includefeatures': True,
            'simplify': False
        }
        url = "".join((self.base_url, "watershed.geojson"))
        response = utils.requests_retry_session().get(url, params=payload)
        response.raise_for_status()  # raises errors early
        return response.json()

    def get_huc(self):
        """Find the Hydrologic Unit Code (HUC) of the watershed."""
        watershed_point = self.data['featurecollection'][0]['feature']
        huc = watershed_point['features'][0]['properties']['HUCID']
        return huc

    def get_boundary(self):
        """Return the full watershed GeoJSON as a dictionary.

        :rtype dict containing GeoJSON watershed boundary
        """
        for dictionary in self.data['featurecollection']:
            if dictionary.get('name', '') == 'globalwatershed':
                return dictionary['feature']
        raise LookupError('Could not find "globalwatershed" in the feature'
                          'collection.')

    def characteristics(self):
        """List the available watershed characteristics.

        Details about these characteristics can be found in the StreamStats
        docs: https://streamstatsags.cr.usgs.gov/ss_defs/basin_char_defs.aspx

        :rtype OrderedDict with characteristic codes and descriptions
        """
        chars = OrderedDict((p['code'], p['name']) for p in self.parameters)
        return chars

    def get_characteristic(self, code=None):
        """Retrieve a specified watershed characteristic

        :param code: Watershed characteristic code to extract.
        :type code: string

        get_characteristic() requires a characteristic code as an argument.
        Valid codes can be seen as keys in the dictionary returned
        by the characteristics() method.

        :rtype dict containing specified characteristic's data and metadata
        """
        keys = list(self.characteristics().keys())
        if code not in keys:
            raise ValueError("code must be a valid key: %s" % ', '.join(keys))
        characteristic_index = keys.index(code)
        characteristic_values = self.parameters[characteristic_index]
        return characteristic_values
