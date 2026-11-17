"""Simple BMI calculator that works with metric or imperial units."""

import warnings


def imperial_to_metric(weight_lb, height_ft):
    """Convert pounds and feet to kilograms and metres."""
    weight_kg = weight_lb * 0.4536
    height_m = height_ft * 0.3048
    return weight_kg, height_m


def calculate_bmi(weight, height, system="metric"):
    """Calculate BMI.

    weight: kilograms for metric, pounds for imperial
    height: metres for metric, feet for imperial
    system: "metric" or "imperial"
    """
    # 1. Check the types of the inputs
    if not isinstance(weight, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("weight and height must be numbers")
    if system not in ("metric", "imperial"):
        raise ValueError("system must be 'metric' or 'imperial'")

    # 2. Check the values make sense
    if weight <= 0 or height <= 0:
        raise ValueError("weight and height must be positive")

    # 3. Warn if the numbers look implausible for the chosen system
    if system == "metric":
        if weight < 2 or weight > 500:
            warnings.warn("weight looks implausible for metric (expected 2-500 kg)")
        if height < 0.6 or height > 2.5:
            warnings.warn("height looks implausible for metric (expected 0.6-2.5 m)")
    else:
        if weight < 4 or weight > 1100:
            warnings.warn("weight looks implausible for imperial (expected 4-1100 lb)")
        if height < 2 or height > 8.2:
            warnings.warn("height looks implausible for imperial (expected 2-8.2 ft)")

    # 4. Convert to metric if needed, then calculate
    if system == "imperial":
        weight, height = imperial_to_metric(weight, height)

    bmi = round(weight / height ** 2, 1)

    return bmi




def interpret_bmi(bmi):
    if bmi < 18.5:
        print(f"Your BMI is {bmi}: underweight")
    elif bmi < 25:
        print(f"Your BMI is {bmi}: normal")
    else:
        print(f"Your BMI is {bmi}: overweight")


if __name__ == "__main__":
    bmi_metric = calculate_bmi(-5, 1.75)
    print(bmi_metric)              # metric
    interpret_bmi(bmi_metric)
    bmi_imperial = calculate_bmi(154, 5.75, "imperial")
    print(bmi_imperial)  # imperial
    interpret_bmi(bmi_imperial)
