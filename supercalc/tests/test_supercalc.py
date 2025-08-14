import pytest

from supercalc import sample_function
def test_supercalc_has_sample_function():
    assert sample_function() is None  # no return value
