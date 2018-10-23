#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for streamstats.finders."""

from streamstats import finders


def test_WatershedFinder():
    # check that we get GeoJSON for valid requests
    f = finders.WatershedFinder()
    r = f.query(state='NY', lon=-74.524, lat=43.939)
    rjson = r.json()
    rjson_keys = rjson.keys()
    assert 'workspaceID' in rjson_keys
    assert 'featurecollection' in rjson_keys
    assert 'parameters' in rjson_keys
    assert 'messages' in rjson_keys
