# -*- coding: utf-8 -*-
"""Tests for streamstats Watershed class."""

import json
import pytest
from vcr_unittest import VCRTestCase
import geojson
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
    def test_get_boundary():
        """check a few random properties of the returned geojson dict"""
        shed = Watershed(lat=43.939, lon=-74.524)
        result = shed.get_boundary()
        geojson_out = geojson.loads(json.dumps(result))
        assert geojson_out.is_valid

    @staticmethod
    def test_characteristics():
        """Check that expected dict keys exist."""
        shed = Watershed(lat=43.939, lon=-74.524)
        obs_keys = shed.characteristics().keys()
        expected_keys = [p['code'] for p in shed.parameters]
        for key in expected_keys:
            assert key in obs_keys

    @staticmethod
    def test_get_characteristic():
        """Get characteristic fails with no argument, succeeds w/ valid arg."""
        shed = Watershed(lat=43.939, lon=-74.524)
        with pytest.raises(ValueError):
            shed.get_characteristic()
        storage = shed.get_characteristic('STORAGE')
        assert storage.get('name') == 'Percent Storage'

    @staticmethod
    def test_get_boundary_raises_error():
        """check that if the data is bad, we get an error"""
        shed = Watershed(lat=43.939, lon=-74.524)
        del shed.data['featurecollection'][1]  # delete the data we need
        message = ''
        try:
            shed.get_boundary()
        except LookupError as error:
            message = str(error)

        assert message == 'Could not find "globalwatershed" in the feature' \
                          'collection.'
