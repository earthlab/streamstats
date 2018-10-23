#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for streamstats.finders."""

from streamstats import finders


def test_WatershedFinder():
    # check that we get GeoJSON for valid requests
    f = finders.WatershedFinder()
    r = f.query(state='NY', lon=-74.524, lat=43.939)
    r_keys = r.keys()
    assert 'workspaceID' in r_keys
    assert 'featurecollection' in r_keys
    assert 'parameters' in r_keys
    assert 'messages' in r_keys
