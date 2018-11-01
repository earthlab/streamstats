# -*- coding: utf-8 -*-
"""Tests for streamstats utility functions."""

import pytest
from vcr_unittest import VCRTestCase
from streamstats import utils


class StreamStatsUtilTests(VCRTestCase):
    '''
    Using a test class based on VCRTestCase allows automatic capture of
    web responses into "cassettes" upon the first run of a given test.
    These cassettes will be "played back" on future tests.
    '''

    @staticmethod
    def test_find_address():
        """Verify that addresses are retrieved."""
        address = utils.find_address(lat=40.0076, lon=-105.2659)
        assert address['city'] == 'Boulder'
        assert address['state'] == 'Colorado'

    @staticmethod
    def test_find_state():
        """Verify that the correct state is returned."""
        address = utils.find_address(lat=40.0076, lon=-105.2659)
        state = utils.find_state(address)
        assert state == 'CO'

    @staticmethod
    def test_canada_raises_errors():
        """Points outside the U.S. should raise errors."""
        with pytest.raises(AssertionError):
            utils.find_address(lat=45.5017, lon=-73.5673)

    @staticmethod
    def test_address_order():
        """Verify that the error message is raised when values are swapped."""
        with pytest.raises(AssertionError):
            utils.find_address(-105.2659, 40.0076)
