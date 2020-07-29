#simply print Aialz Technologies with double quotes use
print("Aialz Technologies")

#simply print Aialz Technologies with single quotes use
print('Aialz Technologies')

# cannot use double quotes twice
#print(""Aialz Technologies"")

# cannot use single quotes twice
#print(''Aialz Technologies'')

#use of double quotes thrice
print("""Aialz Technologies Private Limited""")

#to print As it is
print("""Aialz
Technologies
Private
Limited""")

#use of \n
print("Aialz\nTechnologies\nPrivate\nLimited")

#to print with commas
print("Aialz", "Technologies", "Private", "Limited")

#using seperator(,)
print("Aialz", "Technologies", "Private", "Limited", sep=", ")

#using seperator(/)
print(24,"July", 2020, sep="/")

#print in single sentence with dot
print("Aialz", "Technologies", "Private", "Limited", end=".")

#sep and end together
print("Aialz Technologies", "Bangalore", "Karnataka", sep="\n",end=".")

#sep with two things
print("Aialz Technologies", "Bangalore", "Karnataka", sep=", \n",end=".")

#ending and separating with comma and dot
print('Sun', 'Mon', 'Tue','Wed', sep=', ', end=', ')
print('Thu', 'Fri','Sat', sep=', ', end='. ')

#sep and end together
print("Aialz Technologies","Bangalore","Karnataka",sep=", ", end=".")

#print value of variable
x=70
print(x)

#print value along with statement
x=70
print("x Value is:", x)

# you can't use + sign between 2 different datatype
#x=70
#print("x Values is:" + x)

# str(x) is a type conversion
y = 30
print("y Value is: ", str(y))

#concatenate using +,print values of z along
a=" hello "
b=" world "
z=70
print(a+b,z)

#concatenate using + and converting third variable to str
x=" hello "
y=" world "
z=70
print(x+y+str(z))

#all keywords and length of it
import keyword
print(keyword.kwlist)
print("Total number of keywords ", len(keyword.kwlist))

#can't use a keyword as variable name
#global = 10

#identifiers can be alphabet
x=10
print(x)

#Identifiers can start with "_"
_x=50
print(_x)

#Identifiers cannot start with digits
#1x=20
#print(1x)

#cannot use special symbols like !, @, $, % etc. in our identifier
#x$ = 10

#arithmetic operators
x=5
y=2
print(x + y) #addition
print(x - y) #subtraction(-)
print(x * y) #multiplication(*)
print(x / y) #division(/)
print(x % y) #modulo division (%)
print(x // y) #Floor Division (//)
print(x ** y) #Exponent (**)

#comparison operators
x, y = 10, 20
print(x < y) #check x is less than y
print(x > y) #check x is greater than y
print(x == y) #check x is equal to y
print(x != y) #check x is not equal to y (!=)
print(x >= y) #check x greater than or equal to y
print(x <= y) #check x less than or equal to y

#logical operators
x=True
y=False
print(x and y) #print x and y
print(x or y) #print x or y
print(not y) #print not y

#assignment operator
a=b=c=d=e=f=g=10
a += 5 #add AND
print(a)
b -= 5 #subtract AND (-=)
print(b)
c *= 5 #Multiply AND (*=)
print(c)
d /= 5 #Divide AND (/=)
print(d)
e %= 5 #Modulus AND (%=)
print(e)
f //= 5 #Floor Division (//=)
print(f)
g **= 5 #Exponent AND (**=)
print(g)

#is and is not are the identity operators in Python
x=10
y=20
print(x is y)

#in and not in are the membership operators in Python
x=[10,20,30,40,50]
print(20 in x)
print(20 not in x)

#bitwise operators
x, y = 10, 4
print(x & y) #Bitwise AND
print(x | y) #Bitwise OR
print(~ y) #Bitwise NOT
print(x ^ y) #Bitwise XOR
print(x >> y) #Bitwise rightshift
print(x << y) #Bitwise Leftshift

message='hello world'
#to print length
print(len(message))

#prints only first letter
print(message[0])

#print from start to end position
print(message[0:5])

#print from start to end position without specifying first position
print(message[:5])

#print without last position
print(message[6:])
#lower case
print(message.lower())

#upper case
print(message.upper())

#to count l in it
print(message.count('l'))

#to find world with position
print(message.find('world'))