# Программа проверяет является число положительным
# или отрицательным и выводит следующее сообщение

num = 3

# Также попробовать варианты значения num
# num = -5
# num = 0

if num >= 0:
    print('Число больше или равно нулю')
else:
    print('Число отрицательное')

# str_2 содержит в себе str_1?



def task_yes_no(str_1, str_2):
    if str_1 in str_2:
        print('Да')
    else:
        print('Нет')


str_1 = 'test'
str_2 = 'test1'

task_yes_no(str_1, str_2)


num_float = 3.4
# Попробуйте варианты
num_float = 0
num_float = -4.5

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')


permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')