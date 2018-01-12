# Assignment: Type List
# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.
# Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.
# Here are a couple of test cases. Think of some of your own, too. What kind of unexpected input could you get?

# #input
# l = ['magical unicorns',19,'hello',98.98,'world']
# #output
# "The list you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"


l = ['magical unicorns',19,'hello',98.98,'world']
x_str = []
x_int = []
x_str_final = ""
for x in range (0,len(l)):
    if isinstance(l[x],str):
        x_str.append(l[x])
        x_str_final += l[x]+" "
    if isinstance(l[x],int):
        x_int.append(l[x])
    if isinstance(l[x],float):
        x_int.append(l[x])
if len(x_str) > 0 and len(x_int) > 0:
    print "The list you entered is of mixed type"
    print "String: "+x_str_final
    print "Sum: "+str(sum(x_int))
elif len(x_str) > 0 and len(x_int) == 0:
    print "The list you entered is of string type"
    print "String: "+x_str_final
elif len(x_str) == 0 and len(x_int) > 0:
    print "The list you entered is of integer type"
    print "Sum: "+str(sum(x_int))
else:
    print "The list you entered is of unknown type"

# # input
# l = [2,3,1,7,4,12]
# #output
# "The list you entered is of integer type"
# "Sum: 29"

l = [2,3,1,7,4,12]
x_str = []
x_int = []
x_str_final = ""
for x in range (0,len(l)):
    if isinstance(l[x],str):
        x_str.append(l[x])
        x_str_final += l[x]+" "
    if isinstance(l[x],int):
        x_int.append(l[x])
    if isinstance(l[x],float):
        x_int.append(l[x])
if len(x_str) > 0 and len(x_int) > 0:
    print "The list you entered is of mixed type"
    print "String: "+x_str_final
    print "Sum: "+str(sum(x_int))
elif len(x_str) > 0 and len(x_int) == 0:
    print "The list you entered is of string type"
    print "String: "+x_str_final
elif len(x_str) == 0 and len(x_int) > 0:
    print "The list you entered is of integer type"
    print "Sum: "+str(sum(x_int))
else:
    print "The list you entered is of unknown type"

# # input
# l = ['magical','unicorns']
# #output
# "The list you entered is of string type"
# "String: magical unicorns"

l = ['magical','unicorns']
x_str = []
x_int = []
x_str_final = ""
for x in range (0,len(l)):
    if isinstance(l[x],str):
        x_str.append(l[x])
        x_str_final += l[x]+" "
    if isinstance(l[x],int):
        x_int.append(l[x])
    if isinstance(l[x],float):
        x_int.append(l[x])
if len(x_str) > 0 and len(x_int) > 0:
    print "The list you entered is of mixed type"
    print "String: "+x_str_final
    print "Sum: "+str(sum(x_int))
elif len(x_str) > 0 and len(x_int) == 0:
    print "The list you entered is of string type"
    print "String: "+x_str_final
elif len(x_str) == 0 and len(x_int) > 0:
    print "The list you entered is of integer type"
    print "Sum: "+str(sum(x_int))
else:
    print "The list you entered is of unknown type"

# Think of some of your own, too. What kind of unexpected input could you get?

l = [['magical','unicorns'],[11,12]]
x_str = []
x_int = []
x_str_final = ""
for x in range (0,len(l)):
    if isinstance(l[x],str):
        x_str.append(l[x])
        x_str_final += l[x]+" "
    if isinstance(l[x],int):
        x_int.append(l[x])
    if isinstance(l[x],float):
        x_int.append(l[x])
if len(x_str) > 0 and len(x_int) > 0:
    print "The list you entered is of mixed type"
    print "String: "+x_str_final
    print "Sum: "+str(sum(x_int))
elif len(x_str) > 0 and len(x_int) == 0:
    print "The list you entered is of string type"
    print "String: "+x_str_final
elif len(x_str) == 0 and len(x_int) > 0:
    print "The list you entered is of integer type"
    print "Sum: "+str(sum(x_int))
else:
    print "The list you entered is of unknown type"