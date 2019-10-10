# Write any object: dictionary, string etc to a text file
with open('myfile.txt', 'w') as f:
    print(word_frequencies, file=f)
    
# Check if an object is iterable or not
try:
    iter(jpm)
    print('iteration will probably work')
except TypeError:
    print('not iterable')
