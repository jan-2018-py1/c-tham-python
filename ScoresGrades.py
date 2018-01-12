#  Assignment: Scores and Grades
# Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:
# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A
# The result should be like this:
# Scores and Grades
# Score: 87; Your grade is B
# Score: 67; Your grade is D
# Score: 95; Your grade is A
# Score: 100; Your grade is A
# Score: 75; Your grade is C
# Score: 90; Your grade is A
# Score: 89; Your grade is B
# Score: 72; Your grade is C
# Score: 60; Your grade is D
# Score: 98; Your grade is A
# End of the program. Bye!
# Hint: Use the python random module to generate a random number
# import random
# random_num = random.random()
# # the random function will return a floating point number, that is 0.0 <= random_num < 1.0
# #or use...
# random_num = random.randint()

import random

def score():
    return random.random() * 100

def grades(x):
    if x>=90 and x<=100:
        gd = 'A'
    elif x>=80 and x<=89:
        gd = 'B'
    elif x>=70 and x<=79:
        gd = 'C'
    else:
        gd = 'D'
    print "Score: "+str(x)+"; Your grade is "+gd

print "Scores and Grades"
for x in range(0,10):
    grades(int(score()))
print "End of the program. Bye!"