fname = input('Enter file name: ')
try:
    fhandle = open(fname)
except:
    print('Could not open', fname)
    quit()

hours = dict()

for line in fhandle :
    if line.startswith('From ') :
        words = line.split()
        if len(words) < 6 :
            continue
        time = words[5]
        timeList = time.split(':')
        hour = timeList[0]

        hours[hour] = hours.get(hour, 0) + 1

tupList = sorted(hours.items())
for hour, count in tupList :
    print(hour, count)