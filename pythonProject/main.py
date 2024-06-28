# "Класс «Летающий корабль» (FlyingShip)
#
# Экземпляр класса инициализируется с аргументами: скорость, высота полета, количество пассажиров.
# Класс должен реализовывать методы:
#         change_speed(value) – увеличивает/уменьшпет скорость на значение value, не может быть ниже 0;
#         change_height(value) - изменяет высоту полета на значение value, не может быть ниже 0;
#         add_passengers(value) - добавляет указанное количество пассажиров к текущему количеству;
#         remove_passengers(value) - удаляет указанное количество пассажиров из текущего количества, не может быть меньше 0;
#         get_capacity() - возвращает список из значений: [скорость, высота полета, количество пассажиров].
#         __str()__ - возвращает строку вида: ""FlyingShip with speed <скорость> km/h is flying at an altitude of <высота полета> meters and has <количество пассажиров> passengers"".
#         экземпляры класса можно сравнивать между собой: сначала по количеству пассажиров, затем по скорости, затем по высоте полета.
#
# Создать класс-наследник от класса «Летающий корабль», например, «Истребитель».
#
# Обязательно использование конструктора, декораторов и метода __str__.
# "
from dataclasses import dataclass

@dataclass
class FlyingShip(object):
    # def __init__(self, u, y, amount):
    #     self.u = u
    #     self.y = y
    #     self.amount = amount
    u: float
    y: float
    amount: int
    def change_speed(self, value):
        self.u += value
        if(self.u<0):
            self.u=0
    def change_height(self, value):
        self.y += value
        if(self.y<0):
            self.y=0
    def add_passengers(self,value):
        self.amount += value
    def remove_passengers(self,value):
        self.amount -= value
        if(self.amount<0):
            self.amount = 0
    def get_capacity(self):
        return [self.u, self.y, self.amount]
    def __str__(self):
        print('FlyingShip with speed ',self.u,end=" ")
        print('km/h is flying at an altitude of ', self.y, end=" ")
        print('meters and has ', self.amount, end=" ")
        print('passengers.')
    def __eq__(self, other):
        if isinstance(other, FlyingShip):
            return (self.amount == other.amount and self.u == other.u and self.y == other.y )
        return NotImplemented

@dataclass
class JetRider(FlyingShip):
    # def __init__(self,u,y,amount):
    #     super().__init__(u,y,amount)
    #     self.rocket = 2040
    #     self.chassis = True
    rocket: int = 2040
    chassis: bool = True
    def shoot(self,rocket):
        self.rocket -= rocket
        if(rocket<0):
            rocket = 0
    def rearm(self,rocket):
        self.rocket += rocket
        if(self.rocket > 5000):
            self.rocket = 5000
    def change_chassis(self):
        self.chassis = not(self.chassis)
    def __str__(self):
        super().__str__()
        print ('Ракет: ',self.rocket)
        print('Шасси: ', self.chassis)
ship = FlyingShip(u = 35.0,y = 3000.0,amount = 30)
ship.change_speed(20)
ship.change_height(-4000)
ship.add_passengers(58)
ship.remove_passengers(18)
print(ship.get_capacity())
ship.__str__()
jetpack = JetRider(u = 248,y = 33000,amount = 3)
jetpack.shoot(348)
jetpack.rearm(10400)
jetpack.change_chassis()
jetpack.__str__()
ship2 = FlyingShip(u = 55.0,y = 0.0,amount = 70)
ship3 = FlyingShip(u = 54.0,y = 0.0,amount = 70)
print(ship2 == ship)
print(ship3 == ship)