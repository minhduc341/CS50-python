from seasons import calculate_age_in_minutes
import pytest

def test_calculate_age_in_minutes():
    # Test a valid date of birth
    assert calculate_age_in_minutes("1999-01-01") == 13026240
    assert calculate_age_in_minutes("2023-10-08") == 0

    with pytest.raises(SystemExit):
        calculate_age_in_minutes("2021-13-08")