year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year: 366 days")
        else:
            print("Non-leap year: 365 days")
    else:
        print("Leap year: 366 days")
else:
    print("Non-leap year: 365 days")
