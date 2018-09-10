# 1
number = int(input("Your number"))

action = None
user_action = None

while not action:
    user_action = input("Bytes(b)? or kByte(kb)")
    if user_action == 'b':
        action = 1024
    elif user_action == 'kb':
        action = 1.0 / 1024
    else:
        print("Try again")

print(int(number * action))

# 2 task
number = int(input())

_sum = 0
_mul = 1

while number > 0:
    last_sym = number % 10
    number //= 10
    _sum += last_sym
    _mul *= last_sym

# 3 task
start = input()
end = input()
step = input()

for i in range(start, end, step):
    print(-1.24 * i ** 2 + i)

# 4 task

value = input("Type number")

for i in range(len(value) / 2):
    if value[i] != value[-(i+1)]:
        print('Not palindrome')
        break
else:
    print('Palindrome')

# 5 task
a = [1, 2, -3]

_sum = 0
_count = 0
for value in a:
    if value > 0:
        _sum += value
        _count += 1
print(_sum / (_count or 1))

# new line
# new line in branch branch_1

# line 1
# line 2
# line 3

# line 4
# line 5



