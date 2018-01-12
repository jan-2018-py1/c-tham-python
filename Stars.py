# Assignment: Stars
# Write the following functions.

# Part I
# Create a function called draw_stars() that takes a list of numbers and prints out *.
# For example:
# x = [4, 6, 1, 3, 5, 7, 25]
# draw_stars(x) should print the following when invoked:
# ****
# ******
# *
# ***
# *****
# *******
# *************************

def draw_stars(z):
    star = ''
    for i in range(0,z):
        star += '*'
    return star

x = [4, 6, 1, 3, 5, 7, 25]
for i in range(0,len(x)):
    print draw_stars(x[i])


# Part II
# Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. When a string is passed, instead of displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part.
# For example:
# x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
# draw_stars(x) should print the following in the terminal:
# ****
# ttt
# *
# mmmmmmm
# *****
# *******
# jjjjjjjjjjj


def draw_stars2(z):
    star = ''
    if isinstance(z,int):
        for i in range(0,z):
            star += '*'
    else:
        for i in range(0,len(z)):
            star += z[0]
    return star

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
for i in range(0,len(x)):
    print draw_stars2(x[i])