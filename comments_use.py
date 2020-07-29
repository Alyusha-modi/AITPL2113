#Print Aialz Technologies as output
print("Aialz Technologies")

#Multi line comments
#Can be written using
#hash in the begining of every line

'''Multi line comments
Can be written using three single quotes or
three duoble quotes'''

#using docstring
def add2nums(x,y):
    """
    function to add 2 numbers
    """
    return x+y
print (add2nums(10,40))

print (add2nums.__doc__)
#Docstring is available to us as the attribute __doc__ of the function

#Python Indentation
for i in range(5):
    print(i) #with Indent

#for i in range(5):
#print(i) #without Indent

#indentation can be ignored using in continuation
for i in range(5): print(i)

x = 1 #single statement

#we can make a statement extend over multiple lines with the line continuation character ()
x = 10 + 20 + 30 + \
40 + 50 + 60 + \
70
print (x)

#another way is
x = (10 + 20 + 30 + \
40 + 50 + 60 + \
70)
print (x)

#put multiple statements in a single line using
x = 10; y = 20; z = 30
print(x)
print(y)
print(z)

#assigning same values to each variable in single sentence
x=y=z=10
print(x)
print(y)
print(z)

#can't assign multiple values to one variable
#x=10=20=30=40=50
#print(x)

# Assign multiple values in single line to different variables
x,y,z=50,60,70
print("X Value Is: ",x )
print("y Value Is: ",y )
print("z Value Is: ",z )