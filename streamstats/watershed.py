# -*- coding: utf-8 -*-
"""Functionality for finding watershed information for specific locations."""

import requests
from streamstats import utils


class Watershed():
    """Watershed covering a spatial region, with associated information.

    The USGS StreamStats API is built around watersheds as organizational
    units. Watersheds in the 50 U.S. states can be found using lat/lon
    lookups, along with information about the watershed including its HUC code
    and a GeoJSON representation of the polygon of a watershed. Basin
    characteristics and flow statistics can also be extracted from watersheds.
    """
    base_url = "https://streamstats.usgs.gov/streamstatsservices/"
    url = "".join((base_url, "watershed.geojson"))

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
        self.address = utils.find_address(lat=lat, lon=lon)
        self.data = self._delineate()
        self.workspace = self.data['workspaceID']

    def _delineate(self):
        """Find the watershed that contains a point.

        Implements a Delineate Watershed by Location query from
        https://streamstats.usgs.gov/docs/streamstatsservices/#/

        :rtype dict containing watershed data
        """
        payload = {
            'rcode': utils.find_state(self.address),
            'xlocation': self.lon,
            'ylocation': self.lat,
            'crs': 4326,
            'includeparameters': True,
            'includeflowtypes': False,
            'includefeatures': True,
            'simplify': False
        }
        response = requests.get(self.url, params=payload)
        response.raise_for_status()  # raises errors early
        return response.json()

    def __repr__(self):
        """Get the string representation of a watershed."""
        huc = self.get_huc()
        huc_message = 'Watershed object with HUC%s: %s' % (len(huc), huc)
        coord_message = 'containing lat/lon: (%s, %s)' % (self.lat, self.lon)
        return ', '.join((huc_message, coord_message))

    def get_huc(self):
        """Find the Hydrologic Unit Code (HUC) of the watershed."""
        watershed_point = self.data['featurecollection'][0]['feature']
        huc = watershed_point['features'][0]['properties']['HUCID']
        return huc

    def get_boundary(self):
        """Return the boundary of a watershed as GeoJSON"""
        raise NotImplementedError()

    def available_characteristics(self):
        """List the available watershed characteristics."""
        raise NotImplementedError()

    def get_characteristics(self):
        """Get watershed characteristic data values."""
        raise NotImplementedError()

    def available_flow_stats(self):
        """List the available flow statistics"""
        raise NotImplementedError()

    def get_flow_stats(self):
        """Get watershed flow statistics data values."""
        raise NotImplementedError()
