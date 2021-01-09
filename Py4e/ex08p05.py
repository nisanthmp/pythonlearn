fname = input('Enter file name: ')
try:
    fhandle = open(fname)
except:
    print('Could not open', fname)
    quit()

count = 0
for line in fhandle:
    if line.startswith('From '):
        count += 1
        words = line.split()
        if len(words) < 2 :
            continue
        print(words[1])

print('There were {} lines in the file with From as the first word'.format(count))