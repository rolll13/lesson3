_list = [1, 2, 3]
print(_list)
del _list[0]
print(_list)
del _list[:]
print(_list)
# del a
# print(a)

_dict = {'key1': 1, 'key2': 2}
del _dict['key1']
print(_dict)

# Function


def foo1():
    pass


def foo_with_return():
    return True


def foo_with_params(param1=True, param2=True):
    pass

foo_with_params(False, False)

foo_with_params(param2=False, param1=True)

foo_with_params(False, param2=True)

# DONT DO THIS
#  foo_with_params(param2=True, False)


def foo_args(*args):
    print('FOO ARGS', args)

foo_args(1, 2, 3, 4, 5)


def foo_kwargs(**kwargs):
    print('FOO KWARGS', kwargs)

foo_kwargs(a=1, b=2)

print('#' * 10)


def foo_args_kwargs(*args, **kwargs):
    print('FOO ARGS', args)
    print('FOO KWARGS', kwargs['a'])

foo_args_kwargs(1, 2, 3, 4, 5, a=1, b=2, c=3)


(lambda a, b: a + b)(1, 2)
foo = lambda a, b: a + b


def foo_sum(a, b):
    return a + b


def foo_arr(_list, operation=None):
    result = 0
    for elem in _list:
        result = operation(result, elem)
    return result

print(
    foo_arr([1, 2, 3],
    operation=lambda x, y: x + y)
)
print(
    foo_arr([1, 2, 3],
    operation=lambda x, y: x - y)
)
foo_arr([1,2,3], foo_sum)


# TASK 22
def foo1(x):
    return x ** 2


def foo2(x):
    return 2 * x


def foo3(x):
    return 2 * x - 1


def foo_result(x):
    result = None
    if -5 <= x <= 5:
        result = foo1(x)
    elif x > 5:
        result = foo2(x)
    elif x < -5:
        result = foo3(x)

    return result

arr = []
for i in range(-10, 10, 1):
    arr.append(foo_result(i))

print('Hello world')

