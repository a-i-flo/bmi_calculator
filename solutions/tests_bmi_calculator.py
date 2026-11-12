import pytest

from solutions.bmi_calculator import calculate_bmi, imperial_to_metric


# Checks that pounds and feet are turned into the right kilograms and metres.
def test_imperial_to_metric():
    weight_kg, height_m = imperial_to_metric(154, 5.75)
    assert round(weight_kg, 1) == 69.9
    assert round(height_m, 2) == 1.75


# Checks that the function gives back the correct BMI number for metric inputs.
def test_metric_bmi_returns_value():
    assert calculate_bmi(70, 1.75) == 22.9


# Checks that a normal-weight metric person gets the right printed message.
def test_metric_bmi_normal(capsys):
    calculate_bmi(70, 1.75)
    assert capsys.readouterr().out == "Your BMI is 22.9: normal\n"


# Checks that a normal-weight imperial person gets the right printed message.
def test_imperial_bmi_normal(capsys):
    calculate_bmi(154, 5.75, "imperial")
    assert capsys.readouterr().out == "Your BMI is 22.7: normal\n"


# Checks that a low BMI is labelled as underweight.
def test_underweight(capsys):
    calculate_bmi(50, 1.75)
    assert "underweight" in capsys.readouterr().out


# Checks that a high BMI is labelled as overweight.
def test_overweight(capsys):
    calculate_bmi(90, 1.75)
    assert "overweight" in capsys.readouterr().out


# Checks that we get a warning if someone types height in cm instead of metres.
def test_warns_when_metric_height_given_in_cm():
    with pytest.warns(UserWarning):
        calculate_bmi(70, 175)


# Checks that we get a warning if someone types height in metres instead of feet.
def test_warns_when_imperial_height_given_in_metres():
    with pytest.warns(UserWarning):
        calculate_bmi(154, 1.75, "imperial")


# Checks that text instead of a number for weight is rejected.
def test_type_error_for_string_weight():
    with pytest.raises(TypeError):
        calculate_bmi("70", 1.75)


# Checks that a unit system other than metric or imperial is rejected.
def test_value_error_for_unknown_system():
    with pytest.raises(ValueError):
        calculate_bmi(70, 1.75, "stone")


# Checks that a height of zero is rejected so we never divide by zero.
def test_value_error_for_zero_height():
    with pytest.raises(ValueError):
        calculate_bmi(70, 0)
