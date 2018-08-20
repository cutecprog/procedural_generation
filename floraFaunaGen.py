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
        elif roll <= 0.85:
            self.type = "Herbaceous"
        elif roll <= 0.90:
            self.type = "Algae"
        else:
            self.type = "Fungus"

        self.habitat = {}
        self.grouping = {}
        self.size = {}
        self.body = {}
        self.leaves = {}
        self.reproduction = {}
        self.diet = {}
        self.sentience = {}
        self.edibility = {}

if __name__ == "__main__":
    # execute only if run as a script
    main()