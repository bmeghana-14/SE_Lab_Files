
import pytest
from irrigation_scheduler import should_irrigate, water_volume, schedule


# should_irrigate() branch tests

def test_moisture_greater_than_or_equal_to_60():
    assert should_irrigate(60, 0, "seedling") is False


def test_moisture_below_60():
    assert should_irrigate(40, 0, "seedling") is True


def test_rainfall_greater_than_or_equal_to_10():
    assert should_irrigate(30, 10, "seedling") is False


def test_rainfall_below_10():
    assert should_irrigate(30, 0, "seedling") is True


def test_seedling_moisture_below_45():
    assert should_irrigate(40, 0, "seedling") is True


def test_seedling_moisture_equal_to_45():
    assert should_irrigate(45, 0, "seedling") is False


def test_flowering_moisture_below_55():
    assert should_irrigate(50, 0, "flowering") is True


def test_flowering_moisture_equal_to_55():
    assert should_irrigate(55, 0, "flowering") is False


def test_other_stage_rainfall_greater_than_or_equal_to_5():
    assert should_irrigate(30, 5, "mature") is False


def test_other_stage_rainfall_below_5():
    assert should_irrigate(30, 0, "mature") is True


def test_other_stage_moisture_below_40():
    assert should_irrigate(39, 0, "mature") is True


def test_other_stage_moisture_equal_to_40():
    assert should_irrigate(40, 0, "mature") is False


# water_volume() branch tests

def test_invalid_zero_area():
    with pytest.raises(ValueError):
        water_volume(0, "seedling", 20)


def test_invalid_negative_area():
    with pytest.raises(ValueError):
        water_volume(-5, "seedling", 20)


def test_seedling_stage():
    assert water_volume(10, "seedling", 20) == 20


def test_flowering_stage():
    assert water_volume(10, "flowering", 20) == 50


def test_other_growth_stage():
    assert water_volume(10, "mature", 20) == 40


def test_temperature_above_35():
    assert water_volume(10, "seedling", 36) == 30


def test_temperature_equal_to_35():
    assert water_volume(10, "seedling", 35) == 20


def test_temperature_below_10():
    assert water_volume(10, "seedling", 9) == 10


def test_temperature_equal_to_10():
    assert water_volume(10, "seedling", 10) == 20


# schedule() branch tests

def test_schedule_empty_zones():
    assert schedule([], 100) == []


def test_schedule_zone_needs_no_irrigation():
    zones = [("A", 10, 70, 0, "seedling", 20)]
    assert schedule(zones, 100) == []


def test_schedule_zone_fits_budget():
    zones = [("A", 10, 30, 0, "seedling", 20)]
    assert schedule(zones, 20) == ["A"]


def test_schedule_zone_exceeds_budget():
    zones = [("A", 10, 30, 0, "seedling", 20)]
    assert schedule(zones, 19) == []


def test_schedule_multiple_zones():
    zones = [
        ("A", 5, 30, 0, "seedling", 20),
        ("B", 5, 30, 0, "seedling", 20)
    ]
    assert schedule(zones, 20) == ["A", "B"]
