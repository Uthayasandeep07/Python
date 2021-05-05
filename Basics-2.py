#Type Conversion

a=10
b=123.4
c=a+b
print(c)

# Changing the string number into int

a = 123
b = "456"
print("Data type of num_int:",type(a))
print("Data type of b Before:",type(b))
b = int(b)      # Using this we can type convert
print("Data type of b Now:",type(b))
num_sum = a + b
print("Sum:",num_sum)


# Print Easter Eggs
print(1,2,3,4)      # Prints 1 2 3 4
print(1,2,3,4, sep='^',end='$')     # Prints 1^2^3^4$

#Calling by array index
print('Susan Loves both {0} and {1}'.format('Rolls Royce','Audi')) # prints susan Loves both Rolls royce and Audi


# Getting Input from the User
"""a=input("Enter a Number : ")        # Int
print(a)"""


# Operators

# Arithmetic

a=10
b=5

c=a+b           # Addition
d=a-b           # Subtraction
e=a*b           # Multiply
f=a/b           # Divide
g=a//b          # Floor Division
h=a**b          # Exponent
i=a%b           # Modulus
print(c,d,e,f,g,h,i)

# Comparison Operators 
# Used to compare the values

print('a > b is',a>b)     # Greater than

print('a < b is',a<b)     # Lesser than

print('a == b',a==b)      # Equal to

print('a != b',a!=b)      # Not equal to

print('a >= b',a>=b)      # Greater than or equal to 

print('a <= b',a<=b)      # Less than or equal to


# Logical Operators

a = True
b = False

print('a and b is', a and b)        # And operator -> True if both are true

print('a or b is', a or b)          # Or operator  -> True if any one of the value is true

print('a not operator', not a)      # Not operator -> True if value is false and vice versa


# Bitwise Operators

a = 10   # In Binary (0000 1010)
b = 4    # In Binary (0000 0100)

print('Bitwise AND',a&b)        # Returns (0000 0000)

print('Bitwise OR',a|b)         # Returns (0000 1110) = 14

print('Bitwise NOT',a~b)        # Returns (1111 0101) = -11

print('Bitwise XOR',a^b)        # Returns (0000 1110) = 14

print('Bitwise right shift',a>>b) # Returns (0000 0010) = 2

print('Bitwise left shift',a<<b)  # Returns (0010 1000) = 40


# Assignment Operators
"""
x=10

            =
				x = 5
		

		
			+=
				x += 5              # Expression
				x = x + 5           # Equivalent to
		
			-=
				x -= 5
				x = x - 5
				
			*=
				x *= 5
				x = x * 5
				
			/=
				x /= 5
				x = x / 5
				
			%=
				x %= 5
				x = x % 5
				
			//=
				x //= 5
				x = x // 5
				
			**=
				x **= 5
				x = x ** 5
				
			&=
				x &= 5
				x = x & 5
				
			|=
				x |= 5
				x = x | 5
				
			^=
				x ^= 5
				x = x ^ 5
				
			>>=
				x >>= 5
				x = x >> 5
				
			<<=
				x <<= 5
				x = x << 5

"""