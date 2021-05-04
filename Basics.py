# Common Program

print("Hello world")

# Identifiers
# Represents a Value, Keywords cannot be used as Identifiers

a = 1
print(a)

# Multi Line Statement

b = (1+2+3 +
     4+5+6 +
      7+8+8)
print(b) 

color = ['red','blue','green']
print(color)

# We can also give multiple line statements in a single line
# Like after semicolon

a=1; b=2; c=3
print(a,b,c)

# Assigning Values to Variables

a=10
print(a)

# If we give different value to the same variable it changes
# Let see

a=10
a=5
print(a) # If we execute It comes 5

# Let take output at each step

a=10
print(a)    #prints 10
a=5         #Then later changed to 5
print(a)    #prints 5
a=6         #Again changed to 6
print(a)    #Prints 6

"""So whatever The value is declared to the variable It take the last value
assigned to it"""

# Assigning Multiple values to multiple variables

a,b,c = 10, "Github",22.8
print(a,b,c)


#Assigning same value to Multiple variables

a=b=c=10
print(a,b,c)

# Assigning values from other py documents using ithe another foldermport
import numbers          # Number file is 
print(numbers.b*2)      # Numbers accessed from numbers.py folder and from the variable b  
c=numbers.c             # Assigning to other values to make it functionable
print(c)
print(numbers.b)


# Data Types in python
# Numbers

a = 1
print(a,"is a",type(a))     # type() It prints the data type of a

b=10.5
print(b,"is a",type(b))

c=10+1j
print(c,"is a",type(c))

#If we want to be know as true or false we use

a=10
print(a, "Is it a Number ?", isinstance(10,int))   # Returns TRUE or FALSE


# Python list
# Is an sequence of Items, very flexible. All Kind of datatypes can include. 
# All the items in a list do not need to be of the same type.


a = [5,10,15,"git",25,30,"hub",40]


print("a[2] = ", a[2])          # a[2] = 15

print("a[0:3] = ", a[0:3])      # Prints value from the 0th position untill 3rd position comes a[0:3] = [5, 10, 15]

print("a[5:] = ", a[5:])        # Prints value from the first position

