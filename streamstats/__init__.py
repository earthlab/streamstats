# -*- coding: utf-8 -*-
"""Top-level package for StreamStats."""

__author__ = """Maxwell B. Joseph"""
__email__ = 'maxwell.b.joseph@colorado.edu'
__version__ = '0.1.1'

BASE_URL = "https://streamstats.usgs.gov/streamstatsservices/"

from .watershed import Watershed  # flake8 pylint: noqa
