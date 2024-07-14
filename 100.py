
RATE_FIRST_50_UNITS = 0.30
RATE_NEXT_50_UNITS = 0.50
RATE_ABOVE_100_UNITS = 0.80
units_consumed = 120

if units_consumed <= 50:
    bill = units_consumed * RATE_FIRST_50_UNITS
elif units_consumed <= 100:
    bill = 50 * RATE_FIRST_50_UNITS + (units_consumed - 50) * RATE_NEXT_50_UNITS
else:
    bill = 50 * RATE_FIRST_50_UNITS + 50 * RATE_NEXT_50_UNITS + (units_consumed - 100) * RATE_ABOVE_100_UNITS

# Print the calculated bill
print(f"The water bill for {units_consumed} units is ${bill:.2f}")
