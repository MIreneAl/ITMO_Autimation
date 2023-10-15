class Rest:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width * 2 + self.height * 2


R1 = Rest(5, 6)
print(R1.get_area())
print(R1.get_perimeter())

R2 = Rest(3, 8)
print(R2.get_area())
print(R2.get_perimeter())

R3 = Rest(10, 10)
print(R3.get_area())
print(R3.get_perimeter())


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_addition(self):
        return self.a + self.b

    def get_multiplication(self):
        return self.a * self.b

    def get_division(self):
        return self.a / self.b

    def get_subtraction(self):
        return self.a - self.b


Math = Math(5, 5)
print(Math.get_addition())
print(Math.get_multiplication())
print(Math.get_division())
print(Math.get_subtraction())


class Button:
    def __init__(self, text, mytype='Кнопка', lok=''):
        self.text = text
        self.mytype = mytype
        self.lok = lok

    def cick(self):
        return
