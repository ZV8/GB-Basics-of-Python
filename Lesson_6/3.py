class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return sum(self._income.values())


worker_1 = Position('Иван', 'Петров', 'программист', {"wage": 30000, "bonus": 5000})
print(worker_1.get_full_name())
print(worker_1.get_total_income())
print(worker_1.position)

worker_2 = Position('Николай', 'Иванов', 'барабанщик', {"wage": 24000, "bonus": 7500})
print(worker_2.get_full_name())
print(worker_2.get_total_income())
print(worker_2.position)
