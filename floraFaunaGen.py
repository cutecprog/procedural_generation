"""
Tables by Sebastian Romu

"""
from random import random

def main():
    flora = Flora()
    print("The flora is")
    print("{:>12}: ".format("Type") + flora.type)
    print(vars(flora))

gravity = 0     # Planetary Gravity Index
aura = 0        # Planetary Aura Index
table_names = ["type", "habitat", "grouping", "size", "body", "leaves", \
                "reproduction", "diet", "sentience", "edibility"]

class Flora(object):
    def __init__(self):
        roll = random()
        if roll <= 0.3:
            self.type = "Woody"
            self._woody()
        elif roll <= 0.85:
            self.type = "Herbaceous"
            self._herb()
        elif roll <= 0.90:
            self.type = "Algae"
            self._algae()
        else:
            self.type = "Fungus"
            self._fungus()

        self.habitat = {}
        self.grouping = {}
        self.size = {}
        self.body = {}
        self.leaves = {}
        self.reproduction = {}
        self.diet = {}
        self.sentience = {}
        self.edibility = {}

    def _woody(self):
        roll = random() - 5 * gravity
        print("w")

    def _herb(self):
        print("h")

    def _algae(self):
        print("a")

    def _fungus(self):
        print("f")

    def generate(self):
        if self.type == "Woody":
            self._woody()
        elif self.type == "Herbaceous":
            self._herb()
        elif self.type == "Algae":
            self._algae()
        elif self.type == "Fungus":
            self._fungus()
        else:
            print("Error: type attribute is not valid")

if __name__ == "__main__":
    # execute only if run as a script
    main()