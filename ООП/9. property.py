class Car:
    def __init__(self, brand, model, l_s):
        self.__brand = brand
        self.__model = model
        self.__l_s = l_s

    def __str__(self):
        return 'Марка: {0}\n' \
               'Модель: {1}\n' \
               'Лошадиные силы: {2}'.format(self.__brand, self.__model, self.__l_s)

    @property
    def get_ls(self):
        return self.__l_s

    @get_ls.setter
    def get_ls(self, l_s):
        if isinstance(l_s, int):
            self.__l_s = l_s
        else:
            raise Exception('Нужно число')

    @property
    def get_brand(self):
        return self.__brand

    @get_brand.setter
    def get_brand(self, brand):
        self.__brand = brand

    @property
    def get_model(self):
        return self.__model

    @get_model.setter
    def get_model(self, model):
        self.__model = model




volvo = Car('Volvo', 's40', 344)
volvo.get_ls = 90
volvo.get_brand = 'Марки нет'
volvo.get_model = 'Модели нет'
print(volvo)

