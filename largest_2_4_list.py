print("enter 5 numbers or more:")
list1=[int(x) for x in input().split()]
list1.sort()
if len(list1)>4:
    print("second largest num:{0},fourth largest num:{1}".format(list1[-2],list1[-4]))
else:
    print("invalid entries")