#set of integers
s = {1, 2, 3, 4, 5}
print(s)
#print type of s
print(type(s))

#set doesn't allow duplicates. They store only one instance.
s = {1, 2, 3, 1, 4,5}
print(s)

#we can make set from a list
s = set([1, 2, 3, 1])
print(s)

#initialize a set with set() method
s = set()
print(type(s))

#set object doesn't support indexing
s = {1, 3}
print(s)
#print(s[1]) #will get TypeError

#Adding element to a Set
#add element
s.add(2)
print(s)

#add multiple elements
s = {1, 3}
s.update([5, 6, 1])
print(s)

#add list and set
s.update([8, 9], {10, 2, 3})
print(s)

#A particular item can be removed from set using methods,
#discard() and remove().
s = {1, 2, 3, 5, 4}
print(s)
s.discard(4) #4 is removed from set s
print(s)

s = {1, 2, 3, 5, 4}
print(s)
s.discard(17) #17 is not in set s, it won't show any error
print(s)

s = {1, 2, 3, 5, 4}
print(s)
#remove an element
s.remove(2)
print(s)

#remove an element not present in a set s
#s.remove(7) # will get KeyError

#we can remove item using pop() method
s = {1, 2, 3, 5, 4}
s.pop() #remove random element
print(s)

s.pop()
print(s)

s = {1, 5, 2, 3, 6}
s.clear() #remove all items in set using clear() method
print(s)

#Python Set Operations
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
#union of 2 sets using | operator
print("union of two sets:", set1 | set2)

#another way of getting union of 2 sets,using union function
print(set1.union(set2))

#intersection of 2 sets using & operator
print(set1 & set2)

#use intersection function
print(set1.intersection(set2))

#set Difference: set of elements that are only in set1 but not in set2
print(set1 - set2)

#use differnce function
print(set1.difference(set2))

"""symmetric difference: set of elements in both set1 and set2
except those that are common in both."""
#use ^ operator
print(set1^set2)

#use symmetric_difference function
print(set1.symmetric_difference(set2))

#find issubset()
x = {"a","b","c","d","e"}
y = {"c","d"}
print("set 'x' is subset of 'y' ?", x.issubset(y)) #check x is subset of y
#check y is subset of x
print("set 'y' is subset of 'x' ?", y.issubset(x))

#Frozen Sets
set1 = frozenset([1, 2, 3, 4])
set2 = frozenset([3, 4, 5, 6])
#try to add element into set1 gives an error
#set1.add(5)

# frozen set doesn't support indexing
#print(set1[1])

print(set1 | set2) #union of 2 sets

#intersection of two sets
print(set1 & set2)
#another way
print(set1.intersection(set2))

#symmetric difference
print(set1 ^ set2)
#another way
print(set1.symmetric_difference(set2))