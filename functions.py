# Write any object: dictionary, string etc to a text file
# output should be a string e.g. 'output'
def writeToTxt(output, input):   
    with open(output + '.txt', 'w') as f:
        print(input, file=f)   
        
# saves/downloads a weblink to a location on the hdd        
def saveLink(link, fileName):
    resFile = requests.get(link)
    outFile = open(os.getcwd() + '\\' + fileName, 'wb')
    for chunk in resFile.iter_content(100000):
        outFile.write(chunk)
    outFile.close()  
        
    
# Check if an object is iterable or not
try:
    iter(jpm)
    print('iteration will probably work')
except TypeError:
    print('not iterable')

# Check if a generator has items in it or not    
def isEmpty(iterable):
    try:
        next(iterable)
        return False
    except StopIteration:
        return True
    
