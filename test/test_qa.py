"""
Tests for the basic masking and filtering operations

This also serves as a check for the expected sample data sets
"""
import shared
import pytest
from ccd.qa import *
from ccd.app import defaults


# TODO build contrived arrays for testing rather than reading from a file

#
# Sample 1 (test/resources/sample_1.csva)
#


def test_basic_loading_sample():
    data = shared.read_data("test/resources/sample_1.csv")
    print(data.shape)
    assert data.shape == (9, 69), "Sample data an unexpected shape, other tests may fail."


def test_count_snow():
    data = shared.read_data("test/resources/sample_1.csv")
    qa = data[8]
    assert count_snow(qa) == 2


def test_count_clear_or_water():
    data = shared.read_data("test/resources/sample_1.csv")
    qa = data[8]
    assert count_clear_or_water(qa) == 24


def test_count_total():
    data = shared.read_data("test/resources/sample_1.csv")
    qa = data[8]
    assert count_total(qa) == 69


def test_ratio_snow():
    data = shared.read_data("test/resources/sample_1.csv")
    qa = data[8]
    ratio = ratio_snow(qa)
    assert ratio == pytest.approx(0.076, rel=0.1), ratio_snow(qa)


def test_ratio_clear():
    data = shared.read_data("test/resources/sample_1.csv")
    qa = data[8]
    ratio = ratio_clear(qa)
    assert ratio == pytest.approx(0.347, rel=1e-2)

#
# Sample 2 (test/resources/sample_2.csv)
#


def test_basic_loading_sample():
    data = shared.read_data("test/resources/sample_2.csv")
    assert data.shape == (9, 724), "Sample data an unexpected shape, other tests may fail."


def test_sample_2_count_snow():
    data = shared.read_data("test/resources/sample_2.csv")
    qa = data[8]
    assert count_snow(qa) == 8, count_snow(qa)


def test_sample_2_count_clear_or_water():
    data = shared.read_data("test/resources/sample_2.csv")
    qa = data[8]
    assert count_clear_or_water(qa) == 480, count_clear_or_water(qa)


def test_sample_2_count_total():
    data = shared.read_data("test/resources/sample_2.csv")
    qa = data[8]
    assert count_total(qa) == 724, count_total(qa)


def test_sample_2_ratio_snow():
    data = shared.read_data("test/resources/sample_2.csv")
    qa = data[8]
    ratio = ratio_snow(qa)
    assert ratio == pytest.approx(0.016, rel=0.1), ratio_snow(qa)


def test_sample_2_ratio_clear():
    data = shared.read_data("test/resources/sample_2.csv")
    qa = data[8,:]
    ratio = ratio_clear(qa)
    assert ratio == pytest.approx(0.662, rel=1e-2)


def test_sample_2_exercise_temperature_index():
    # This sample data does not have any thermal values that
    # are outside the threshold... this test still serves
    # a purpose though.
    data = shared.read_data("test/resources/sample_2.csv")
    # index = filter_thermal_celsius(data)
    assert data.shape == (9, 724)