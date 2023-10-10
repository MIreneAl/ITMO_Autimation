class Button:

    def __init__(self, text, link):
        self.text = text
        self.link = link


# создаем экземпляры класса
home = Button('Домой', '/ home')
catalog_msk = Button('Каталог', '/msk/catalog')

# Получаем доступ к атрибутам
print(home.text)
print('Кнопка' + home.text + 'Имеет ссылку' + home.link)

print('\n')

print(catalog_msk.text)
print('Кнопка' + catalog_msk.text + 'Имеет ссылку' + catalog_msk.link)


class Button_Two:

 def __init__(self, text, link, lok):
    self.text = text
    self.link = link
    self.lok = lok


def click(self):
    return "Клик по локатору - {}" .format(self.lok)

#Создаем экземпляры класса

home_two = Button_Two ('Домой', '/home', 'button#home')

# Вызываем метод

print(home_two.click())