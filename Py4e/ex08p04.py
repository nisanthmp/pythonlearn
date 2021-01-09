fname = input('Enter file name: ')
try:
    fhandle = open(fname)
except:
    print('Could not open', fname)
    quit()

words = list()
for line in fhandle:
    wordsInLine = line.split()
    for word in wordsInLine:
        if word not in words:
            words.append(word)

words.sort()
print(words)