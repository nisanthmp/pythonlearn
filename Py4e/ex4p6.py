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

def computepay(hrs, rate) :
    if hrs <= 40 :
        return (hrs * rate)
    else :
        return (40 * rate + (hrs - 40) * rate * 1.5)

print("Pay", computepay(hrs, rate))
