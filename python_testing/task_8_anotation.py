a: int = 5
b: str = 'строка'
c: list = [1, 2]


def indent(s: str, width: int) -> str:
    return "" * (max(0, width - len(s)))+s


print(indent('123', 123))


def indent_len(str1='') -> int:
    s = len(str1)
    return s


print(indent_len('Мир'))


def indenty_len( mylist, list1) -> int:
    a = len (mylist)
    b = len(list1)
    return max(a, b)

p1 = [12,4,5,67,7]
p2 = [48,2]
result = indenty_len(p1,p2)
print(result)

def letter(mylist):
    mylist.append('o')
    return mylist

l1 = ['a', 'b', 'c']
print(letter(l1))

def my_list (listsum) ->int:
    sum_of_list = sum(listsum)
    return sum_of_list

print(my_list([1, 2, 3, 4]))