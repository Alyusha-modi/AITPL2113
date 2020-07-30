#Tuple creation
t = () #empty tuple
#tuple having integers
t = (1, 2, 3)
print(t)
#tuple with mixed datatypes
t = (1, 'xyz', 28, 'abc')
print(t)
#nested tuple
t = (1, (2, 3, 4), [1, 'xyz', 28, 'abc'])
print(t)

#only parenthesis is not enough
a = ('alyusha')
print(type(a))

#need a comma at the end
b = ('alyusha',)
print(type(b))

#parenthesis is optional
t = "alyusha",
print(type(t))
print(t)

#Accessing Elements in Tuple
t = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(t[4])

#negative index
print(t[-1]) #print last element in a tuple

#nested tuple
t = ('Mon', ('Tue', 'Wed', 'Thu'))
print(t[0])
print(t[1])
print(t[1][1])

#Slicing
t = (1, 2, 3, 4, 5, 6)
print(t[1:4])
#print elements from starting to 2nd last elements
print(t[:-2])
#print elements from starting to end
print(t[:])

#Changing a Tuple
t = (1, 2, 3, 4, [5, 6, 7])
#t[2] = 'x' #will get TypeError

#list inside a tuple can be changed
t = (1, 2, 3, 4, [5, 6, 7])
print(t)
t[4][1] = 100
print(t)

#concatinating tuples using + operator
t = (1, 2, 3) + (4, 5, 6)
print(t)

#repeat the elements in a tuple for a given number of times using the * operator
t = (('Alyusha', ) * 4)
print(t)

#we cannot change the elements in a tuple.

#delete entire tuple using del keyword throws an error
t = (1, 2, 3, 4, 5, 6)
print(t)
#delete entire tuple
print(t)

#get the frequency of particular element appears in a tuple
t = (1, 2, 3, 1, 3, 3, 4, 1)
print(t.count(1))

#print index of the 70
t = (10, 20, 70, 10, 70, 30, 70, 10)
print(t.index(70)) #returns index of the element is equal to 2

#test if an item exists in a tuple or not, using the keyword in.
t = (1, 2, 3, 4, 5, 6)
print(1 in t)
print(7 in t)

#counting length of tuple using len function
t = (1, 2, 3, 4, 5, 6)
print(len(t))

#Tuple Sort
t = (4, 5, 1, 2, 3)
new_t = sorted(t)
print(new_t) #Take elements in the tuple and return a new sorted list
#(does not sort the tuple itself).

#get the largest element in a tuple
t = (2, 5, 1, 6, 9)
print(max(t))

#get the smallest element in a tuple
print(min(t))

#get sum of elments in the tuple
print(sum(t))

