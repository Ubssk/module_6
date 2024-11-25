from random import randint


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    _cords = [0, 0, 0]
    def __init__(self, speed):
        self.speed = speed

    def move(self, dx, dy, dz):
        self.dx = self.speed * dx
        self.dy = self.speed * dy
        self.dz = self.speed * dz
        if self.dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = [self.dx, self.dy, self.dz]

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        elif self._DEGREE_OF_DANGER == 5 or self._DEGREE_OF_DANGER > 5:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(f"Строка со звуком: {self.sound}")

class Bird(Animal):
    beak = True
    def lay_eggs(self):
        print(f"Here are(is) {randint(1,4)} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def __init__(self, speed):
        super().__init__(speed)

    def dive_in(self, dz):
        self.dz = abs(self.speed//2 *dz)
        self._cords[2] = self.dz

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    def __init__(self, speed):
        super().__init__(speed)
        self.sound = "Click-click-click"


db = Duckbill(10)



print(db.live)

print(db.beak)



db.speak()

db.attack()



db.move(1, 2, 3)

db.get_cords()

db.dive_in(6)

db.get_cords()



db.lay_eggs()