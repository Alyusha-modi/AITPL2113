
def pallindrome_check(s):
    s=s.lower()
    rev=s[::-1]
    if s==rev:
        print("Its pallindrome")
    else:
        print("It is not pallindrome")

print("enter any string to check pallindrome")
s=input()
pallindrome_check(s)