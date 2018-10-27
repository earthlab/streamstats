# -*- coding: utf-8 -*-
"""Tests for streamstats utility functions."""

import pytest
from streamstats import utils


def test_find_address():
    """Verify that addresses are retrieved."""
    address = utils.find_address(lat=40.0076, lon=-105.2659)
    assert address['city'] == 'Boulder'
    assert address['state'] == 'Colorado'


def test_find_state():
    """Verify that the correct state is returned."""
    address = utils.find_address(lat=40.0076, lon=-105.2659)
    state = utils.find_state(address)
    assert state == 'CO'


def test_canada_raises_errors():
    """Points outside the U.S. should raise errors."""
    with pytest.raises(AssertionError):
        utils.find_address(lat=45.5017, lon=-73.5673)
