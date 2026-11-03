
import pytest
from irrigation_scheduler import should_irrigate, water_volume, schedule


def test_wet_soil_no_irrigation():
    assert should_irrigate(70, 0, "seedling") is False


def test_rainfall_at_limit_prevents_irrigation():
    assert should_irrigate(30, 10, "seedling") is False


def test_seedling_dry_soil_needs_irrigation():
    assert should_irrigate(40, 0, "seedling") is True


def test_seedling_moisture_not_low_enough():
    assert should_irrigate(50, 0, "seedling") is False


def test_flowering_stage_needs_irrigation():
    assert should_irrigate(50, 0, "flowering") is True


def test_flowering_stage_moist_enough():
    assert should_irrigate(55, 0, "flowering") is False


def test_other_stage_rainfall_at_five():
    assert should_irrigate(30, 5, "mature") is False


def test_other_stage_soil_below_threshold():
    assert should_irrigate(30, 0, "mature") is True


def test_other_stage_soil_at_threshold():
    assert should_irrigate(40, 0, "mature") is False


def test_seedling_volume():
    assert water_volume(10, "seedling", 20) == 20


def test_flowering_volume():
    assert water_volume(10, "flowering", 20) == 50


def test_other_stage_volume():
    assert water_volume(10, "mature", 20) == 40


def test_area_must_be_positive():
    with pytest.raises(ValueError, match="invalid area"):
        water_volume(0, "seedling", 20)


def test_hot_temperature_multiplier():
    assert water_volume(10, "seedling", 36) == 30


def test_cold_temperature_multiplier():
    assert water_volume(10, "seedling", 9) == 10


def test_normal_temperature_no_multiplier():
    assert water_volume(10, "seedling", 20) == 20


def test_schedule_adds_irrigated_zone():
    zones = [("A", 10, 30, 0, "seedling", 20)]
    assert schedule(zones, 100) == ["A"]


def test_schedule_skips_zone_that_does_not_need_water():
    zones = [("A", 10, 70, 0, "seedling", 20)]
    assert schedule(zones, 100) == []


def test_schedule_stops_when_budget_is_insufficient():
    zones = [("A", 10, 30, 0, "seedling", 20)]
    assert schedule(zones, 19) == []


def test_schedule_continues_after_skipping_a_zone():
    zones = [
        ("Wet", 10, 70, 0, "seedling", 20),
        ("Dry", 10, 30, 0, "seedling", 20),
    ]
    assert schedule(zones, 100) == ["Dry"]


def test_schedule_uses_remaining_budget():
    zones = [
        ("First", 5, 30, 0, "seedling", 20),
        ("Second", 10, 30, 0, "seedling", 20),
    ]
    assert schedule(zones, 15) == ["First"]
