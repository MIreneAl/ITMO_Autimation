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