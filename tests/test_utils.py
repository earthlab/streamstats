# -*- coding: utf-8 -*-
"""Tests for streamstats utility functions."""

import pytest
from streamstats import utils


@pytest.fixture
@pytest.mark.vcr()
def address():
    """A fixture for the address of Boulder, CO."""
    return utils.find_address(lat=40.0076, lon=-105.2659)


def test_find_address(address):
    """Verify that addresses are retrieved."""
    assert address['city'] == 'Boulder'
    assert address['state'] == 'Colorado'


def test_find_state(address):
    """Verify that the correct state is returned."""
    state = utils.find_state(address)
    assert state == 'CO'


@pytest.mark.vcr()
def test_canada_raises_errors():
    """Points outside the U.S. should raise errors."""
    with pytest.raises(AssertionError):
        utils.find_address(lat=45.5017, lon=-73.5673)
