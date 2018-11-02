# -*- coding: utf-8 -*-
"""Tests for streamstats utility functions."""

import pytest
from streamstats import utils


@pytest.mark.vcr()
def test_find_address():
    """Verify that addresses are retrieved."""
    address = utils.find_address(lat=40.0076, lon=-105.2659)
    assert address['city'] == 'Boulder'
    assert address['state'] == 'Colorado'


@pytest.mark.vcr()
def test_find_state():
    """Verify that the correct state is returned."""
    address = utils.find_address(lat=40.0076, lon=-105.2659)
    state = utils.find_state(address)
    assert state == 'CO'


@pytest.mark.vcr()
def test_canada_raises_errors():
    """Points outside the U.S. should raise errors."""
    with pytest.raises(AssertionError):
        utils.find_address(lat=45.5017, lon=-73.5673)


@pytest.mark.vcr()
def test_find_address_err_mess():
    """Error message provides lat & lon in correct order."""
    try:
        utils.find_address(lat=40, lon=-200)
    except ValueError as err:
        message = str(err)
    assert ("lat=40" in message) and ("lon=-200" in message)
