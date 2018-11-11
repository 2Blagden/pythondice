#import random. This will allow random integers to be generated easily.
import random
#forever:
while True:
#variable j is a string taken from user input.
    j = input("type p to roll")
#if variable j is the same as string "p": 
    if j == "p":
#print (log to console) a random integer between 1 and 6.
        print(random.randint(1, 6))
#value of j set to null. This causes loop to go back to asking the user for an input.
        j = ""