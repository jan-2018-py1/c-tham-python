# Assignment: String and List Practice
# Use only the built-in methods and functions from the previous tabs to do the following exercises. You will find the following methods and functions useful:
# • .find()
# • .replace()
# • min()
# • max()
# • .sort()
# • len()

# Find and Replace
# In this string: words = "It's thanksgiving day. It's my birthday,too!" print the position of the first instance of the word "day". Then create a new string where the word "day" is replaced with the word "month".

words = "It's thanksgiving day. It's my birthday,too!"
std1 = 'day'
print words.find(std1)
std2 = 'month'
# print words.replace(std1,std2)
words_new = words.replace(std1,std2)
print words_new

# Min and Max
# Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

# First and Last
# Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list. Your code should work for any list.

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[len(x)-1]
x_new = [x[0],x[len(x)-1]]
print x_new

# New List
# Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!

### why .sort is not working? ###

x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x_new = sorted(x)
print x_new
half = len(x) / 2
print half
x_half1 = []
x_half2 = []
for i in range(0, half):
    x_half1.append(x_new[i])
print x_half1
x_half2.append(x_half1)
for i in range(half, len(x)):
    x_half2.append(x_new[i])
print x_half2
