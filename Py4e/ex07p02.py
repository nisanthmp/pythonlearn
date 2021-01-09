pattern = 'X-DSPAM-Confidence:'

fileName = input('Enter the file name: ')
try:
    fileHandle = open(fileName, 'r')
except:
    print('Failed open file:', fileName)
    quit()

count = 0
total = 0.0

for line in fileHandle :
    if not line.startswith(pattern) :
        continue
    count += 1
    colPos = line.find(':')
    sVal = line[colPos + 1 : ]
    total += float(sVal)

if count == 0 :
    avg = 0
else :
    avg = total/count

print('Average spam confidence:', avg)
