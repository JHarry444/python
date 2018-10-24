class Vehicle:
    def __init__(self, wheelnum):
        self.wheelNumber = wheelnum

    def getwheelnumber(self):
        return self.wheelNumber


class Car(Vehicle):
    def __init__(self):
        Vehicle.__init__(self, 4)


bmw = Car()
print(bmw.getwheelnumber())
