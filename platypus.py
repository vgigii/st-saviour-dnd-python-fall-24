from mammal import Mammal

class Platypus(Mammal):
    def __init__(self, name : str, species : str, hair_color : str, eggs: int):
        super().__init__(name, species, hair_color)
        self.eggs = eggs

    def lay_egg(self):
        self.eggs += 1

    def __str__(self):
        return f'name{}