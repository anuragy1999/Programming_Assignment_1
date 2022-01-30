# 1.Write a Python program to print "Hello Python"?
print("Hello Python")

# 2.Write a Python program to do arithmetical operations addition and division ?
a= int(input("Enter a number"))
b= int(input("Enter a number"))
c=a+b
d=a/b
print(c,d)

# 3.Write a Python program to find the area of a triangle?
a= int(input("Enter a height"))
b= int(input("Enter a base"))
c= 0.5*(a*b)
print(c)

# 4.Write a Python program to swap two variables?
a= int(input("Enter a number1"))
b= int(input("Enter a number2"))
c,d=0,0
print(a,b)
d,c=b,a
print(d,c)

# 5.Write a Python program to generate a random number?
import random
print(random.randint(0,9))
