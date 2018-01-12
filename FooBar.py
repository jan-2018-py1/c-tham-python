# Optional Assignment: Foo and Bar
# Write a program that prints all the prime numbers and all the perfect squares for all numbers between 100 and 100000.
# For all numbers between 100 and 100000 test that number for whether it is prime or a perfect square. If it is a prime number, print "Foo". If it is a perfect square, print "Bar". If it is neither, print "FooBar". Do not use the python math library for this exercise. For example, if the number you are evaluating is 25, you will have to figure out if it is a perfect square. It is, so print "Bar".
# This assignment is extra challenging! Try pair programming and pulling up a whiteboard.

# test for prime number
for i in range(1,20):
    prime = False
    for j in range(2,i):
        if float(i%j) == 0.0:
            break
    else:
        prime = True
    if prime == True:
        print i

# test for perfect square
for i in range(0,100):
    # print str(i)+' '+str(i**0.5)+' '+str((i**0.5)**2)+' '+str(float(i))
    # if float(i) == ((i**0.5)**2):
    #     print 'Square'
    if float(i) == ((i**0.5)**2) and (int(i**0.5)-(i**0.5)) == 0:
        print str(float(i))+' is Perfect Square'

# Write a program that prints all the prime numbers and all the perfect squares for all numbers between 100 and 100000.

for i in range(100,1000):
    prime = False
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        prime = True
    if prime == True:
        print str(i)+' is Prime'
    if float(i) == ((i**0.5)**2) and (int(i**0.5)-(i**0.5)) == 0:
        print str(i)+' is Perfect Square = '+str(i**0.5)

# For all numbers between 100 and 100000 test that number for whether it is prime or a perfect square. If it is a prime number, print "Foo". If it is a perfect square, print "Bar". If it is neither, print "FooBar". Do not use the python math library for this exercise. For example, if the number you are evaluating is 25, you will have to figure out if it is a perfect square. It is, so print "Bar".


for i in range(100,1000):
    prime = ''
    square = ''
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        prime = 'Foo'
    if float(i) == ((i**0.5)**2) and (int(i**0.5)-(i**0.5)) == 0:
        square = 'Bar'
    print str(i)+' '+prime+square

