fname = input('Enter file name: ')
try:
    fhandle = open(fname)
except:
    print('Could not open', fname)
    quit()

committers = dict()

for line in fhandle :
    if line.startswith('From ') :
        words = line.split()
        if len(words) < 2 :
            continue
        committer = words[1]
        committers[committer] = committers.get(committer, 0) + 1

mostCommitter = None
mostCommits = None

for committer, count in committers.items() :
    if (mostCommitter is None) or (count > mostCommits) :
        mostCommitter = committer
        mostCommits = count

print(mostCommitter, mostCommits)