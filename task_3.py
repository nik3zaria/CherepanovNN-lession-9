

class Worker():

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f'Фамилия и Имя: {self.name} {self.surname}'

    def get_total_income(self):
        return f'self._income['wage'] + self._income['bonus'] рублей за расчетный месяц.'




if __name__ == '__main__':
    dictionary_of_income_data = {'wage': 33, 'bonus': 15}
    user_data = Position('vova', 'petrov', 'man of steel', dictionary_of_income_data,)
    print(user_data.get_total_income())
    print(user_data.get_full_name())