from animal import Animal

class Mammal(Animal):
    def __init__(self, name: str, species: str, hair_color: str):
        super().__init__(name, species)
        self.warm_blooded = True
        self.hair_color = hair_color

    def sleep(self):
        print(self.name + ' the ' + self.hair_color + ' ' + self.species + ' falls asleep...')
