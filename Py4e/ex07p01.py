fileName = input('Enter the file name: ')
try:
    fileHandle = open(fileName, 'r')
except:
    print('Failed to open file', fileName)
    quit()

fileContent = fileHandle.read()
fileContent = fileContent.rstrip()

uFileContent = fileContent.upper()
print(uFileContent)