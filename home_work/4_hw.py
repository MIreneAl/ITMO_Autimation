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

    def click(self):
        return "Клик по кнопке " + self.text


Button1 = Button('Text Box')
Button2 = Button('Check Box')
Button3 = Button('Radio Button')
Button4 = Button('Web Tables')
Button5 = Button('Button')
Button6 = Button('Links')
Button7 = Button('Broken Links - Images')
Button8 = Button('Upload and Download')
Button9 = Button('Dynamic Properties')
Button10 = Button('Practice Form')
Button11 = Button('Browser Windows')
Button12 = Button('Alerts')
Button13 = Button('Frames')
Button14 = Button('Nested Frames')
Button15 = Button('Modal Dialogs')
Button16 = Button('Accordian')
Button17 = Button('Auto Complete')
Button18 = Button('Data Picker')
Button19 = Button('Slider')
Button20 = Button('Progress Bar')
Button21 = Button('Tabs')
Button22 = Button('Tool Tips')
Button23 = Button('Menu')
Button24 = Button('Select Menu')
Button25 = Button('Sortable')
Button26 = Button('Selectable')
Button27 = Button('Resizable')
Button28 = Button('Droppable')
Button29 = Button('Dragabble')
Button30 = Button('Login')
Button31 = Button('Book Store')
Button32 = Button('Profile')
Button33 = Button('Book Store API')
print(Button1.click())
print(Button2.click())
print(Button3.click())
print(Button4.click())
print(Button5.click())
print(Button6.click())
print(Button7.click())
print(Button8.click())
print(Button9.click())
print(Button10.click())
print(Button11.click())
print(Button12.click())
print(Button13.click())
print(Button14.click())
print(Button15.click())
print(Button16.click())
print(Button17.click())
print(Button18.click())
print(Button19.click())
print(Button20.click())
print(Button21.click())
print(Button22.click())
print(Button23.click())
print(Button24.click())
print(Button25.click())
print(Button26.click())
print(Button27.click())
print(Button28.click())
print(Button29.click())
print(Button30.click())
print(Button31.click())
print(Button32.click())
print(Button33.click())