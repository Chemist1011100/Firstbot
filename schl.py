import random
def nums():
    num = random.randint(0,7)
    return num
def numb():
    nub = random.randint(0,4)
    return nub
class Rabotnik():
    def __init__(self):
        self.names = ['Антон', 'Борис', 'Виталий', 'Геннадий', 'Денис', 'Елисей', 'Саша', 'Игорь']
        self.surnames = ['Абрамов', 'Быков', 'Васнецов', 'Гагарин', 'Дорохов', 'Ельцин', 'Слюсарь', 'Ивлев']
        self.fathname = ['Антонович', 'Борисович', 'Виталиевич', 'Генадиевич', 'Денисович', 'Елисеевич', 'Евгениевич', 'Львович']
        self.year = [2002, 2003, 2004, 2005, 2006]
        self.money = [0, 15000, 20000, 35000, 100000]
    def worker_info(self):
        print(f"ФИО:{self.surnames[nums()]} {self.names[nums()]} {self.fathname[nums()]}; Год рождения: {self.year[numb()]}; Зарплата: {self.money[numb()]} рублей")
work1 = Rabotnik()
work1.worker_info()
