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
    
# Fetching environment variables from the env file (option 1)
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_FOLDER = 'C:\\repo\\'
env_file = BASE_FOLDER + "\\.env"
load_dotenv(dotenv_path=env_file)

ORACLE_USER = os.getenv("ORACLE_USER")
ORACLE_PWD = os.getenv("ORACLE_PWD")

# Fetching environment variables from the env file (option 2)
# This technique is smart as it uses the path of this script to find the working directory
# But the disadvantage is that it cannot be used in the python interactive terminal 
# Because python terminal doesn't know the location of the file, but the terminal (e.g. cmd) does
BASE_FOLDER = os.path.realpath(os.path.dirname(__file__))
print(BASE_FOLDER) # Just to be sure

from dotenv import load_dotenv
env_file = BASE_FOLDER + "\\.env"
load_dotenv(dotenv_path=env_file)

ORACLE_USER = os.getenv("ORACLE_USER")
ORACLE_PWD = os.getenv("ORACLE_PWD")

print(ORACLE_USER) # Just to be sure
print(ORACLE_PWD) # Just to be sure
