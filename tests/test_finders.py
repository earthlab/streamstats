#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for streamstats.finders."""

import pytest
from streamstats import finders


def test_find_watershed():
    """Verify that the JSON response contains expected keys."""
    resp = finders.find_watershed(lon=-74.524, lat=43.939)
    resp_keys = resp.keys()
    assert 'workspaceID' in resp_keys
    assert 'featurecollection' in resp_keys
    assert 'parameters' in resp_keys
    assert 'messages' in resp_keys


def test_find_state():
    """Verify that the correct state is returned."""
    state = finders.find_state(-103.376294, 39.7392)
    assert state == 'CO'


def test_canada_raises_errors():
    """Points outside the U.S. should raise errors."""
    with pytest.raises(AssertionError):
        finders.find_state(-73.5673, 45.5017)
