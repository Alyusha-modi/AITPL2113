print("enter numbers:")
list1=[int(x) for x in input().split()]
new_list = set(list1)
new_list.remove(max(new_list))
new_list1=new_list.copy()

new_list1.remove(max(new_list1))

new_list1.remove(max(new_list1))
print("second largest number:", max(new_list))
print("fourth largest number:", max(new_list1))
