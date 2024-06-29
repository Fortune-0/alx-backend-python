#!/usr/bin/env python3
"""
fixtures.py - Fixtures for setting up and tearing down the test environment
"""

import pytest


@pytest.fixture
def example_fixture():

    """
    Example fixture that sets up the test environment.

    Yields:
        None
    """
    print("Setting up the test environment")
    yield
    print("Tearing down the test environment")
