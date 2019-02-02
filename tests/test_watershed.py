# -*- coding: utf-8 -*-
"""Tests for streamstats Watershed class."""

import json
import pytest
import geojson
from streamstats import Watershed


@pytest.fixture
@pytest.mark.vcr()
def shed():
    """A watershed object to use across tests."""
    return Watershed(lat=43.939, lon=-74.524)


def test_watershed(shed):
    """Verify that the JSON response contains expected keys."""
    keys = shed.data.keys()
    assert 'workspaceID' in keys
    assert 'featurecollection' in keys
    assert 'parameters' in keys
    assert 'messages' in keys
    assert '04150305' in str(shed)
    assert str(shed.lat) in str(shed)
    assert str(shed.lon) in str(shed)


def test_boundary(shed):
    """check a few random properties of the returned geojson dict"""
    result = shed.boundary
    geojson_out = geojson.loads(json.dumps(result))
    assert geojson_out.is_valid


def test_characteristics(shed):
    """Check that expected dict keys exist."""
    obs_keys = shed.characteristics.keys()
    expected_keys = [p['code'] for p in shed.parameters]
    for key in expected_keys:
        assert key in obs_keys


def test_get_characteristic(shed):
    """Get characteristic fails with no argument, succeeds w/ valid arg."""
    with pytest.raises(ValueError):
        shed.get_characteristic()
    storage = shed.get_characteristic('STORAGE')
    assert storage.get('name') == 'Percent Storage'


def test_boundary_raises_error(shed):
    """check that if the data is bad, we get an error"""
    del shed.data['featurecollection'][1]  # delete the data we need
    with pytest.raises(LookupError, match='Could not find "globalwatershed"'):
        shed.boundary
