# Import libraries  
import time
import string
import random
import urllib.request
import sys

# load the hamlet text and conver it into a list of lowercase chars 
url = r'http://www.gutenberg.org/files/1524/1524-0.txt'
bytedata = urllib.request.urlopen( url ).read()
data=bytedata.decode()
charlist = [c.lower() for c in data if c.isalpha()]  # 150012 characters 

# Record start time
start_time = time.time()

# logic to time how long it would take to randomly write hamlet
while(1):
  index = 0
  while(1):
    # if index reaches end hamlet has been typed
    if(index == len(charlist)):
       print('\n' + "The program took " + str((time.time() - start_time)))
       sys.exit() # exit program 
    # randomly choose a character and compare it with the character needed to type hamlet 
    elif(random.choice(string.ascii_lowercase) != charlist[index]):
      break # if not correct break and try again 
    index +=1
