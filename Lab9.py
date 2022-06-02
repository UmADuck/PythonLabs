class Animal:
    def __init__(self, name: str, predatory: bool, legs: int = 4, eyes: int = 2):
        self.name = name
        self.predatory = predatory
        self.legs = legs
        self.eyes = eyes

class Mammal(Animal):
    def __init__(self, name: str, has_fur: bool , predatory: bool, legs: int = 4, eyes: int = 2):
        super().__init__(name, predatory, legs, eyes)
        self.has_fur = has_fur

    def __str__(self):
        return f"{str(self.__class__)}:  {str(self.__dict__)}"

class Bird(Animal):
    def __init__(self, name: str, has_feather: bool , predatory: bool, legs: int = 4, eyes: int = 2):
        super().__init__(name, predatory, legs, eyes)
        self.has_feather = has_feather

    def __str__(self):
        return f"{str(self.__class__)}:  {str(self.__dict__)}"

class Insect(Animal):
    def __init__(self, name: str, can_fly: bool, predatory: bool, legs: int = 4, eyes: int = 2):
        super().__init__(name, predatory, legs, eyes)
        self.can_fly = can_fly

    def __str__(self):
        return f"{str(self.__class__)}:  {str(self.__dict__)}"

class Reptile(Animal):
    def __init__(self, name: str, can_swim: bool, predatory: bool, legs: int = 4, eyes: int = 2):
        super().__init__(name, predatory, legs, eyes)
        self.can_swim = can_swim

    def __str__(self):
        return f"{str(self.__class__)}:  {str(self.__dict__)}"

class Fish(Animal):
    def __init__(self, name: str, has_scales: bool, predatory: bool, legs: int = 4, eyes: int = 2):
        super().__init__(name, predatory, legs, eyes )
        self.has_scales = has_scales

    def __str__(self):
        return f"{str(self.__class__)}:  {str(self.__dict__)}"

mammal = Mammal("wolf", True,  True)
print(mammal)

bird = Bird("Crow", True,  True, 2)
print(bird)

insect = Insect("fly", True,  True, 6, 6)
print(insect)

reptile = Reptile("crocodile", True,  True)
print(reptile)

fish = Fish("salmon", True,  False, 0)
print(fish)

