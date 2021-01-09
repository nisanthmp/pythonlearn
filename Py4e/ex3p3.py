score_str = input("Enter a score between 0.0 and 1.0: ")

try:
    score = float(score_str)
except:
    print("Entered not a number")

if (score < 0.0) or (score > 1.0) :
    print("Entered score is out of range (0.0, 1.0)")
    quit()

if score >= 0.9 :
    print("A")
elif score >= 0.8 :
    print("B")
elif score >= 0.7 :
    print("C")
elif score >= 0.6 :
    print("D")
else :
    print("F")
