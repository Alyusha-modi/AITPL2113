x = [] #Empty list
l1 = ['Aialz', 'Technologies', 'Private', 'Limited'] # list of strings
l2 = [1, 2, 3, 4] #list of integers
l3 = [[1, 2], [3, 4]] # list of lists
l4 = [1, 'Aialz Technologies', 24, 1.24] # list of different datatypes
print(x)
print(l1)
print(l2)
print(l3)
print(l4)

#length of list
l2=[10,20,30,40,50]
print(len(l2))
l1 = ['one', 'two', 'three', 'four']
#find length of a list
print(len(l1))

#to add elements at the last of the string
l2=[10,20,30,40,50]
l2.append(60)
print(l2)

l1 = ['one', 'two', 'three', 'four']
l1.append('five') # append will add the item at the end
print(l1)

lst = ['one', 'two', 'four']
lst.insert(2, "three") # will add element y at location x
print(lst)

l2=[10,20,30,40,50]
l2.insert(4,100)
print(l2)

#syntax: list.remove(x)
l1 = [10,20,30,40,50,20,20]
l1.remove(20) #it will remove first occurence of '20' in a given list
print(l1)

#syntax: list.remove(x)
l1 = [10,20,30,40,50]
#l1.remove(70) #it will remove first occurence of '70' in a given list if it finds, otherwise it throughs the error
print(l1)

l1 = [10,20,30,40,50]
del l1[2] #it will remove first occurence of '30' in a given list
print(l1)

#append list in list
l1 = ['one', 'two', 'three', 'four']
l2 = ['five', 'six']
l1.append(l2)
print(l1)

l1 = ['one', 'two', 'three', 'four']
l2 = ['five', 'six']
#extend will join the list with list1
l1.extend(l2)
print(l1)

#del to remove item based on index position
l1 = ['one', 'two', 'three', 'four', 'five']
del l1[1]
print(l1)
l1 = ['one', 'two', 'three', 'four', 'five'] #or we can use pop() method
popvalue=l1.pop(1)
print(popvalue)
print(l1)

l1 = ['one', 'two', 'three', 'four']
#remove an item from list
l1.remove('three')
print(l1)

#keyword 'in' is used to test if an item is in a list
l1 = ['one', 'two', 'three', 'four']
if 'two' in lst:
    print('two in the list')

#keyword 'not' can combined with 'in'
if 'six' not in lst:
    print('six not in the list')

#reverse - reverses the entire list
l1 = ['one', 'two', 'three', 'four']
l1.reverse()
print(l1)

#create a list with numbers
l1 = [4, 7,5 , 2, 8]
sorted_l1 = sorted(l1)
print("Sorted list :", sorted_l1)
#original list remain unchanged
print("Original list: ", l1)

#create a list with numbers
l1 = [4, 7, 5, 2, 8]
#print a list in reverse sorted order
print("Reverse sorted list :", sorted(l1, reverse=True))
#orginal list remain unchanged
print("Original list :", l1)

l1 = [1, 20, 5, 4, 4.2]
#sort the list and stored in itself
l1.sort()
# add element 'a' to the list to show an error
print("Sorted list: ", l1)

#l1 = [17, 2, ,'e','b', 5, 'a']
#print(l1.sort()) # sort list with element of different datatypes

#List Having Multiple References
l1 = [10, 20, 30, 40, 50]
l2 = l1
l2.append(60)
#print original list
print("Original list: ", l1)
print("Original list: ", l2)

#String Split to create a list
#let's take a string
sl1 = "one,two,three,four,five"
sl2 = sl1.split(',')
print(sl2)

sl1 = "Aialz Technologies Private Limited"
split_sl2 = sl1.split() # default split is white-character: space or tab
print(split_sl2)

l1 = [10, 20, 30, 40,50]
print(l1[1]) #print second element
#print last second element using negative index
print(l1[-2])

#List Slicing
l1 = [10, 20, 30, 40, 50,60,70,80]
print(l1[:]) #print all numbers
print(l1[0:4]) #print from index 0 to index 3
print(l1[-4:-1]) #print from index -4 to index -2
print(l1[-4:]) #print from index -4 to index -1
print(l1[-1::-5]) #print from index -1 and index -6

l1 = [10, 20, 30, 40, 50,60,70,80]
print (l1)
#print alternate elements in a list
print(l1[::2])
#print elements alternatively start from 2
print(l1[2::2])
#print elements alternatively start from 1
print(l1[1::2])

#List extend using "+"
l1 = [1, 2, 3, 4]
l2 = ['Aialz', 'technologies', 'Private', 'Limited']
l3 = l1 + l2
print(l3)

#List Count
l1 = [10, 20, 50, 10, 50, 40, 20, 50]
#frequency of 10 in a list
print(l1.count(10))
#frequency of 50 in a list
print(l1.count(50))

#loop through a list
l1 = ['one', 'two', 'three', 'four']
for i in l1:
    print(i)