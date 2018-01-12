# Assignment: Compare Lists
# Write a program that compares two lists and prints a message depending on if the inputs are identical or not.
# Your program should be able to accept and compare two lists: list_one and list_two. If both lists are identical print "The lists are the same". If they are not identical print "The lists are not the same." Try the following test cases for lists one and two:

# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
list1 = len(list_one)
list2 = len(list_two)
list_same = False
if list1 > list2 or list2 > list1:
    print "The lists are not the same."
else:
    for x in range(0, list1):
        if (list_one[x] == list_two[x]):
            list_same = True
        else:
            list_same = False
    if list_same == True:
        print "The lists are the same"
    else:
        print "The lists are not the same."

# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
list1 = len(list_one)
list2 = len(list_two)
list_same = False
if list1 > list2 or list2 > list1:
    print "The lists are not the same."
else:
    for x in range(0, list1):
        if (list_one[x] == list_two[x]):
            list_same = True
        else:
            list_same = False
    if list_same == True:
        print "The lists are the same"
    else:
        print "The lists are not the same."

# list_one = [1,2,5,6,5,16]
# list_two = [1,2,5,6,5]

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
list1 = len(list_one)
list2 = len(list_two)
list_same = False
if list1 > list2 or list2 > list1:
    print "The lists are not the same."
else:
    for x in range(0, list1):
        if (list_one[x] == list_two[x]):
            list_same = True
        else:
            list_same = False
    if list_same == True:
        print "The lists are the same"
    else:
        print "The lists are not the same."

# list_one = ['celery','carrots','bread','milk']
# list_two = ['celery','carrots','bread','cream']

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
list1 = len(list_one)
list2 = len(list_two)
list_same = False
if list1 > list2 or list2 > list1:
    print "The lists are not the same."
else:
    for x in range(0, list1):
        if (list_one[x] == list_two[x]):
            list_same = True
        else:
            list_same = False
    if list_same == True:
        print "The lists are the same"
    else:
        print "The lists are not the same."
