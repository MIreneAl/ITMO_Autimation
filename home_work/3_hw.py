def num(a, b):
    if a == b + 135 or a == b - 135:
        print('yes')
    else:
        print('No')


num(135, 0)


def num(c, d):
    if c > d:
        print('c')
    else:
        print('d')


num(5, 10)


def season_year(number_of_month):
    if number_of_month in range(3, 5):
        print('Весна')
    elif number_of_month in range(6, 8):
        print('Лето')
    elif number_of_month in range(9, 11):
        print('осень')
    else:
        print('Зима')


season_year(4)


def num(x, y, z):
    if x > 10 and y > 10 and z > 10:
        print('Yes')
    else:
        print('No')


num(11, 45, 2)


def kolvo(mylist):
    k = 0
    for nun in mylist:
        if nun >= 0:
            k = k+1
    print (k)


kolvo([1, -8, 5, 0, 2])

