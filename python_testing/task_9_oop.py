class Button:

    def __init__(self, text, link):
        self_text = text
        self_link = link


# создаем экземпляры класса
home = Button('Домой', '/ home')
catalog_msk = Button('Каталог', '/msk/catalog')

# Получаем доступ к атрибутам
print(home.text)
print('Кнопка' + home.text + 'Имеет ссылку' + home.link)

print('\n')