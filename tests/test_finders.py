#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for streamstats.finders."""

from streamstats import finders


def test_find_watershed():
    """Verify that the JSON response contains expected keys."""
    resp = finders.find_watershed(state='NY', lon=-74.524, lat=43.939)
    resp_keys = resp.keys()
    assert 'workspaceID' in resp_keys
    assert 'featurecollection' in resp_keys
    assert 'parameters' in resp_keys
    assert 'messages' in resp_keys
