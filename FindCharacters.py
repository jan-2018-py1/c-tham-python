# Assignment: Find Characters
# Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.
# Here's an example:
# # input
# word_list = ['hello','world','my','name','is','Anna']
# char = 'o'
# # output
# new_list = ['hello','world']
# Hint: how many loops will you need to complete this task?

word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_list = []
for x in range(0,len(word_list)):
    for y in range(0,len(word_list[x])):
        if word_list[x][y] == char:
            new_list.append(word_list[x])
print word_list
print new_list