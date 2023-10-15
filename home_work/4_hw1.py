class Car:
    def __init__(self, color='', mtype='', year=''):
        self.color = color
        self.mtype = mtype
        self.year = year

    def lanch(self):
        print('Автомобиль заведен')

    def shutdown(self):
        print('Автомобиль заглушен')

    def fyear(self, year):
        self.year = year
        print('Присвоен год выпуска ' + year)

    def fmtype(self, mtype):
        self.mtype = mtype
        print('Присвоен тип ' + mtype)

    def fcolor(self, color):
        self.color = color
        print('Присвоен цвет ' + color)


Avto = Car()
Avto.lanch()
Avto.shutdown()
Avto.fcolor('Белый')
Avto.fyear('2022')
Avto.fmtype('Nissan')
