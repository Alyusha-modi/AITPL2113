def check_prime():
    for num in range(m, n + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

print("Enter the interval:")
m,n=[int(x) for x in input().split()]
check_prime()