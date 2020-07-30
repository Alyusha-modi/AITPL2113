#Dict Creation

#empty dictionary
my_dict = {}

#dictionary with integer keys
my_dict = {1: 'abc', 2: 'xyz'}
print(my_dict)

#dictionary with mixed keys
my_dict = {'name': 'Alyusha', 1: ['abc', 'xyz']}
print(my_dict)

#create empty dictionary using dict()
my_dict = dict()
my_dict = dict([(1, 'abc'), (2, 'xyz')]) #create a dict with list of tuples
print(my_dict)

my_dict = {'fname': 'Alyusha', 'lname': 'Modi', 'city': 'Bhagalpur'}
#get fname
print(my_dict['fname'])

#if key is not present it gives KeyError
#print(my_dict['dob'])

#another way of accessing key using get method
print(my_dict.get('city'))

#if key is not present it will give None using get method
print(my_dict.get('Country'))

#Dict Add or Modify Elements
my_dict = {'fname': 'Alyusha', 'lname': 'modi', 'city': 'Bhagalpur'}
#update fname
my_dict['fname'] = 'Rani'
print(my_dict)

#adding new key
my_dict['state'] = 'bihar'
print(my_dict)

#Dict Delete or Remove Element
#create a dictionary
my_dict = {'fname': 'Harsh', 'lname': 'Vardhan', 'city': 'forbesganj'}
#remove a particular item using pop method
print(my_dict.pop('lname'))
print(my_dict)

my_dict = {'fname': 'Ian', 'lname': 'somerhalder', 'city': 'Los Angeles'}
#remove an arbitarty key using popitem method
my_dict.popitem()
print(my_dict)

#delete particular  using del
d = {2: 4, 3: 9, 4: 16, 5: 25}
del d[2]
print(d)

d = {2: 4, 3: 9, 4: 16, 5: 25}
print(d)
#remove all items using clear method
d.clear()
print(d)

#delete dictionary itself using del command
d = {2: 4, 3: 9, 4: 16, 5: 25}
del d
#print(d) #NameError because dict is deleted

#using copy function we can copy from on dictionary to another
d = {2: 4, 3: 9, 4: 16, 5: 25}
my_dict = d.copy()
print(my_dict)

