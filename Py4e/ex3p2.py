hrs_str = input("Enter Hours: ")
try:
    hrs = float(hrs_str)
except:
    print("Entered not a number")
    quit()

rate_str = input("Enter Rate: ")
try:
    rate = float(rate_str)
except:
    print("Entered not a number")
    quit()

if hrs <= 40 :
    print(hrs * rate)
else :
    print(40 * rate + (hrs - 40) * rate * 1.5)
