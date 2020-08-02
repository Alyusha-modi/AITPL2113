
def index(i):
    return 1 + (i >> 31) - (-i >> 31)


def type_of_num(n):
    # string array to store all kinds of number
    kind = "negative", "zero", "positive"

    # function call to check the sign of number
    val = index(n)

    print(n, "is", kind[val])

print("Enter a number to check")
p=int(input())
type_of_num(p)



