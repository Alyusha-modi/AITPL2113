count=1
num=1
print("Enter the number of rows")
rows=int(input())
space=rows-1
for i in range(1,rows):
    for j in range(1,space):
        print(end=" ")

    for k in range(1,num):
        print(count%2,end="")
        count=count+1
    space=space-1
    num=num+2
    print()