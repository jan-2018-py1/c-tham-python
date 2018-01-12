# Assignment: Coin Tosses
# Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
# Sample output should be like the following:
# Starting the program...
# Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
# Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
# Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
# Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
# ...
# Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
# Ending the program, thank you!
# Hint: Use the python built-in round function to convert that floating point number into an integer
# x = .23945593
# y = .798839238
# x_rounded = round(x)
# # x_rounded will be rounded down to 0
# y_rounded = round(y)
# # y_rounded will be rounded up to 1

import random

def coin():
    return int(round(random.random()))

head = 0
tail = 0
print "Starting the program..."
for i in range(0,50):
    x = coin()
    if x == 0:
        head += 1
        side = "head"
    else:
        tail += 1
        side = "tail"
    # print x, head, tail
    print "Attempt #"+str(i)+": Throwing a coin... It's a "+side+"! ... Got "+str(head)+" head(s) so far and "+str(tail)+" tail(s) so far"
print "Ending the program, thank you!"
