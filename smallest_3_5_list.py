print("enter numbers:")
list1=[int(x) for x in input().split()]
list1.sort()
if len(list1)>5:
    print("third smallest num:{0},fifth smallest num:{1}".format(list1[2],list1[4]))
else:
    print("invalid entries")