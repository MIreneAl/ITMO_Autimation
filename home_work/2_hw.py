def task_1() -> None:
    x: int = 28
    y: float = 3.14159
    l: list = [1, 2, 3, 4, 5]
    p: str = 'hello word'
    z: bool = True
    print('значение ', x, 'имеет тип ', type(x))
    print('значение ', y, 'имеет тип ', type(y))
    print('значение ', l, 'имеет тип ', type(l))
    print('значение ', p, 'имеет тип ', type(p))
    print('значение ', z, 'имеет тип ', type(z))


task_1()


def task_2() -> list:
    a = [1, 2, 3, 5, 8, 13, 21]
    return a[0:3]


print('a{0:3]=', task_2())


def task_3(x: int) -> int:
    return x * x


print(task_3(2))