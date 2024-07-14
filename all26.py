is_weekday = True
is_holiday = False
is_raining = False
is_sunny = True
print("Logical Operators with Boolean Values:")
and_result = is_weekday and is_sunny
print(f"is_weekday and is_sunny: {and_result}")  
or_result = is_raining or is_sunny
print(f"is_raining or is_sunny: {or_result}")    
not_result = not is_holiday
print(f"not is_holiday: {not_result}")           
complex_result = (is_weekday and is_sunny) or (is_holiday and is_raining)
print(f"((is_weekday and is_sunny) or (is_holiday and is_raining)): {complex_result}")
another_complex_result = (is_weekday and not is_raining) or (not is_sunny and is_holiday)
print(f"((is_weekday and not is_raining) or (not is_sunny and is_holiday)): {another_complex_result}")



