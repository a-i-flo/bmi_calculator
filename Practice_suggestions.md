# Practice suggestions

Each exercise follows the same pattern as the BMI calculator. Write one small Python
module with a function that does the job, then write a pytest file for it. Put a
one-line comment above each test saying in plain words why that test is needed.

For every exercise your tests should cover:

- at least one normal case with a known answer
- the edges where the answer changes
- bad input that should raise an error
- input that is technically valid but looks wrong and should raise a warning

Keep printing out of the function you are testing. Return a value and let a separate
piece of code print it.

## 1. Temperature converter

Write a program that converts a temperature between Celsius, Fahrenheit and Kelvin.
The user gives a number, the unit it is in, and the unit they want.

- Converting a unit to itself should give the number back unchanged.
- Temperatures below absolute zero are impossible and should be rejected.
- A unit that is not one of the three should be rejected.
- Everyday temperatures outside roughly -90 to 60 Celsius should still work but produce
  a warning.

## 2. Running pace

Write a program that takes a distance and a time in minutes and tells the runner their
pace. The runner can choose metric (minutes per kilometre) or imperial (minutes per mile).

- The distance and time must both be positive.
- The unit system must be metric or imperial, nothing else.
- A pace faster than about 2 minutes per kilometre is not humanly possible and should
  produce a warning. So should a pace slower than about 30 minutes per kilometre.

## 3. Heart rate zones

Write a program that takes a person's age and their current heart rate in beats per
minute and tells them which training zone they are in. Use the common rule that maximum
heart rate is 220 minus age, and split the range into zones such as rest, light,
moderate, hard and maximum.

- Age and heart rate must be positive whole numbers.
- A heart rate higher than the calculated maximum should produce a warning.
- An age below 10 or above 100 should produce a warning.
- Make sure the zone boundaries are tested exactly, not just values in the middle.

## 4. Age calculator

Write a program that works out how old someone is on a given day from their date of
birth. Pass both dates in, so the answer does not depend on when the tests run.

- A date of birth in the future should be rejected.
- Inputs that are not dates should be rejected.
- Check the day before a birthday, the birthday itself, and the day after.
- Check someone born on 29 February in a year that is not a leap year.

## 5. Savings calculator

Write a program that works out how much a sum of money grows to when interest is added
regularly. The user gives the starting amount, the yearly interest rate, the number of
years, and how many times per year interest is added.

- A rate of zero should give back the starting amount.
- Negative amounts, years or rates should be rejected.
- Compare your answer to a known textbook example. Floating point results will not be
  exactly equal, so use pytest.approx.
- A rate given as 5 when 0.05 was meant should still work but produce a warning.
