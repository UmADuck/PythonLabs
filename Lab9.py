class Animals:
    def __init__(self, name, predatory, legs = 4, eyes = 2):
        self.name = name
        self.predatory = predatory
        self.legs = legs
        self.eyes = eyes

class Mammals(Animals):
    def __init__(self, name, has_fur, predatory, legs = 4, eyes = 2):
        super().__init__(name, legs, eyes, predatory)
        self.has_fur = has_fur

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

class Birds(Animals):
    def __init__(self, has_feather, name, predatory, legs = 4, eyes = 2):
        super().__init__(name, legs, eyes, predatory)
        self.has_feather = has_feather

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

class Insects(Animals):
    def __init__(self, can_fly, name, predatory, legs = 4, eyes = 2):
        super().__init__(name, legs, eyes, predatory)
        self.can_fly = can_fly

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

class Reptiles(Animals):
    def __init__(self, can_swim, name, predatory, legs = 4, eyes = 2):
        super().__init__(name, legs, eyes, predatory)
        self.can_swim = can_swim

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

class Fish(Animals):
    def __init__(self, has_scales, name, predatory, legs = 4, eyes = 2):
        super().__init__(name, legs, eyes, predatory)
        self.has_scales = has_scales

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

mammal = Mammals(True, "wolf", True)
print(mammal)

bird = Birds(True, "Crow", True, 2)
print(bird)

insect = Insects(True, "fly", True, 6, 6)
print(insect)

reptile = Reptiles(True, "crocodile", True)
print(reptile)

fish = Fish(True, "salmon",  False, 0)
print(fish)

