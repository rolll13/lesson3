print('Task 1')


def symbol_type():
    symbol = input('input letter: ')
    if 96 < ord(symbol) < 123:
        print("It's English letter")
    else:
        print("Other symbol")


symbol_type()

print('Task 2')


def factorial(x):
    j = 1
    for i in range(x):
        i += 1
        j *= i
    print(j)

factorial(int(input('Input number: ')))

print('Task 3')


def multiplication_table():
    for multiplier_1 in range(9):
        multiplier_1 += 1
        print('For: ', multiplier_1)
        for multiplier_2 in range(9):
            multiplier_2 += 1
            print(multiplier_1, '*', multiplier_2,
                  '=',multiplier_1*multiplier_2 )

multiplication_table()