# -*- coding: utf-8 -*-
"""Tests for streamstats Watershed class."""

from vcr_unittest import VCRTestCase
from streamstats import Watershed


class WatershedUnitTests(VCRTestCase):
    '''
    Using a test class based on VCRTestCase allows automatic capture of
    web responses into "cassettes" upon the first run of a given test.
    These cassettes will be "played back" on future tests.
    '''

    @staticmethod
    def test_find_watershed():
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
        result = shed.get_geojson()
        assert result['type'] == 'FeatureCollection'
        assert result['features'][0]['properties']['I6H2Y'] == 1.263
        assert result['features'][0]['properties']['LC11DEV'] == 100
        assert result['features'][0]['bbox'][2] == -105.24254752674744
        assert result['features'][0]['geometry']['coordinates'][0][00][1] \
            == 40.006538265576346

    @staticmethod
    def test_get_geojson_raises_error():
        """check that if the data is bad, we get an error"""
        shed = Watershed(40.009631, -105.242433)
        del shed.data['featurecollection'][1]  # delete the data we need
        message = ''
        try:
            shed.get_geojson()
        except LookupError as error:
            message = str(error)

        assert message == 'Could not find "globalwatershed" in the feature' \
                          'collection.'

    @staticmethod
    def test_get_boundary():
        """test the bounding box for a given case"""
        shed = Watershed(40.009631, -105.242433)
        result = shed.get_boundary()

        assert result == [-105.2410132678883, 40.009688732073656,
                          -105.24254752674744, 40.00653802187368]
