hrs_str = input("Enter Hours: ")
rate_str = input("Input Rate: ")

hrs = float(hrs_str)
rate = float(rate_str)

if hrs <= 40 :
    print(hrs * rate)
else :
    print(40 * rate + (hrs - 40) * rate * 1.5)
