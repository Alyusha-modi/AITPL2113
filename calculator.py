def calculate():
    choice = int(input('''
Please type in the math operation you would like to complete:
1 for addition
2 for subtraction
3 for multiplication
4 for division
'''))

    n1 = int(input('Please enter the first number: '))
    n2 = int(input('Please enter the second number: '))

    if choice == 1:
        print('{} + {} = '.format(n1, n2))
        print(n1 + n2)

    elif choice == 2:
        print('{} - {} = '.format(n1, n2))
        print(n1 - n2)

    elif choice == 3:
        print('{} * {} = '.format(n1, n2))
        print(n1 * n2)

    elif choice == 4:
        print('{} / {} = '.format(n1, n2))
        print(n1 / n2)

    else:
        print('Invalid command')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to continue?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Thankyou!')
    else:
        again()

calculate()