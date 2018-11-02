# -*- coding: utf-8 -*-
"""Tests for streamstats Watershed class."""

from vcr_unittest import VCRTestCase
from streamstats import Watershed


class WatershedUnitTests(VCRTestCase):
    """
    Using a test class based on VCRTestCase allows automatic capture of
    web responses into "cassettes" upon the first run of a given test.
    These cassettes will be "played back" on future tests.
    """

    @staticmethod
    def test_watershed():
        """Verify that the JSON response contains expected keys."""
        wshed = Watershed(lat=43.939, lon=-74.524)
        keys = wshed.data.keys()
        assert 'workspaceID' in keys
        assert 'featurecollection' in keys
        assert 'parameters' in keys
        assert 'messages' in keys
        assert '04150305' in str(wshed)
        assert str(wshed.lat) in str(wshed)
        assert str(wshed.lon) in str(wshed)

    @staticmethod
    def test_get_geojson():
        """check a few random properties of the returned geojson dict"""
        shed = Watershed(40.009631, -105.242433)
        result = shed.get_boundary()
        assert 'type' in result.keys()
        assert 'crs' in result.keys()
        assert 'features' in result.keys()
        assert 'properties' in result['features'][0].keys()
        assert 'type' in result['features'][0].keys()
        assert 'bbox' in result['features'][0].keys()
        assert 'geometry' in result['features'][0].keys()
        assert 'coordinates' in result['features'][0]['geometry'].keys()

    @staticmethod
    def test_get_geojson_raises_error():
        """check that if the data is bad, we get an error"""
        shed = Watershed(40.009631, -105.242433)
        del shed.data['featurecollection'][1]  # delete the data we need
        message = ''
        try:
            shed.get_boundary()
        except LookupError as error:
            message = str(error)

        assert message == 'Could not find "globalwatershed" in the feature' \
                          'collection.'

    @staticmethod    
    def test_flow_stats():
        """Verify that we get the expected flow statistics"""
        wshed = Watershed(lat=43.939, lon=-74.524)
        stats = wshed.get_flow_stats()
        assert stats[0].keys() == stats[1].keys()

        available_stats = wshed.available_flow_stats()
        assert len(available_stats) == 2
        assert len(stats) == len(available_stats)
        assert 'Peak-Flow Statistics' in available_stats
        assert 'Bankfull Statistics' in available_stats
