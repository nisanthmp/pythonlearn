text = "X-DSPAM-Confidence:    0.8475"

colPos = text.find(':')
snum = text[colPos + 1 : ]
#snum = snum.strip()
num = float(snum)
print(num)
