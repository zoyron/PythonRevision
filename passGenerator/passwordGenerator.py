#this is a mini project that will generate a random password of length 12


import random

lower  = "abcdefghijklmnopqrstuvwxyz"
upper  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,_"
allToConsiderForPassword = lower + upper + numbers + symbols

length = 12

password = "".join(random.sample(allToConsiderForPassword, length))
print(password)
