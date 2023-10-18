from task_9_checks import Checks


class Input(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text


class Button(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text


class Title(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text


class Link(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text


search = Input('input#search', 'Поиск')

print(search.loc, search.text)

home_three = Button('button#home_three', 'Домой')

print(home_three.loc, home_three.text)

test = Title('title#test', 'Заголовок')

print(test.loc, test.text)

search_two = Link('link#search_two', 'Связь')

print(search_two.loc, search_two.text)