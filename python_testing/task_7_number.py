def task_func(a=(1, 2, 3, 4)):
    return a[1]

print(task_func())


def arg(a, b, c=2, d=3):
    return a + b + c + d

print (arg(1, 1, 1, 1))

print(arg(2, 2))


def range_arg(a, b, c, d):
    return a + '' + b + '' + c + '' + d

print(range_arg('1', '2', '3', '4'))

print(range_arg('1', '2', c='4', d='3'))


def computer_funk(r, pi=3.14159):
    return r*r*pi


print(computer_funk(2))