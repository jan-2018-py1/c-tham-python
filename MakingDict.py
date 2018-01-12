# Assignment: Making Dictionaries
# Create a function that takes in two lists and creates a single dictionary. The first list contains keys and the second list contains the values. Assume the lists will be of equal length.
# Your first function will take in two lists containing some strings. Here are two example lists:
# name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
# favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
# Here's some help starting your function.
# def make_dict(list1, list2):
#   new_dict = {}
#   # your code here
#   return new_dict

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
    new_dict = {}
    if len(list1) >= len(list2):
        new_dict = zip(list1, list2)
    else:
        new_dict = zip(list2, list1)
    return new_dict

print make_dict(name, favorite_animal)

# Hacker Challenge:
# If the lists are of unequal length, the longer list should be used for the keys, the shorter for the values.

def make_dict2(list1, list2):
    new_dict = {}
    if len(list1) >= len(list2):
        new_dict = zip(list1, list2)
    else:
        new_dict = zip(list2, list1)
    return new_dict

lt1 = ["1","2","3"]
lt2 = ["a","b"]

print make_dict2(lt1,lt2)


lt1 = ["1","2"]
lt2 = ["a","b","c"]

print make_dict2(lt1,lt2)