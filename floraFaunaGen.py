"""
Tables by Sebastian Romu

"""
from random import random

def main():
    flora = Flora()
    print("The flora is")
    print("{:>12}: ".format("Type") + flora.type)
    print(vars(flora))
    print(select(random(), \
            {"Woody": 0.30, "Herbaceous": 0.85, "Algae": 0.90, "Fungus": 1}))

gravity = 0     # Planetary Gravity Index
aura = 0        # Planetary Aura Index
table_names = ["type", "habitat", "grouping", "size", "body", "leaves", \
        "reproduction", "diet", "sentience", "edibility"]

def select(roll, weights):
    for tag in sorted(weights, key=weights.get):
        # sort table able by weights
        if roll <= weights[tag]:
            return tag

class Flora(object):
    def __init__(self):
        self.habitat = {}
        self.grouping = {}
        self.size = {}
        self.body = {}
        self.leaves = {}
        self.reproduction = {}
        self.diet = {}
        self.sentience = {}
        self.edibility = {}
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

    def _woody(self):
        roll = random() - 5 * gravity
        if roll <= 0.05:
            self.habitat["primary"] = "Aquatic"
        elif roll <= 0.1:
            self.habitat["primary"] = "Sub-Terrestrial"
        elif roll <= 0.99:
            self.habitat["primary"] = "Terrestrial"
        else:
            self.habitat["primary"] = "Avian"

        roll = random()
        if self.habitat["primary"] == "Aquatic":
            if roll <= 0.3:
                self.habitat["sub"] = "Salt-Water"
            elif roll <= 0.9:
                self.habitat["sub"] = "Fresh Water"
            else:
                self.habitat["sub"] = "Brackish"

    def _herb(self):
        roll = random() - 5 * gravity
        if roll <= 0.35:
            self.habitat["primary"] = "Aquatic"
        elif roll <= 0.4:
            self.habitat["primary"] = "Sub-Terrestrial"
        elif roll <= 0.99:
            self.habitat["primary"] = "Terrestrial"
        else:
            self.habitat["primary"] = "Avian"

        roll = random()
        if self.habitat["primary"] == "Aquatic":
            if roll <= 0.3:
                self.habitat["sub"] = "Salt-Water"
            elif roll <= 0.9:
                self.habitat["sub"] = "Fresh Water"
            else:
                self.habitat["sub"] = "Brackish"

    def _algae(self):
        roll = random() - 5 * gravity
        if roll <= 0.8:
            self.habitat["primary"] = "Aquatic"
        elif roll <= 0.9:
            self.habitat["primary"] = "Sub-Terrestrial"
        elif roll <= 0.98:
            self.habitat["primary"] = "Terrestrial"
        else:
            self.habitat["primary"] = "Avian"

        roll = random()
        if self.habitat["primary"] == "Aquatic":
            if roll <= 0.3:
                self.habitat["sub"] = "Salt-Water"
            elif roll <= 0.9:
                self.habitat["sub"] = "Fresh Water"
            else:
                self.habitat["sub"] = "Brackish"

    def _fungus(self):
        roll = random() - 5 * gravity
        if roll <= 0.1:
            self.habitat["primary"] = "Aquatic"
        elif roll <= 0.4:
            self.habitat["primary"] = "Sub-Terrestrial"
        elif roll <= 0.99:
            self.habitat["primary"] = "Terrestrial"
        else:
            self.habitat["primary"] = "Avian"

        roll = random()
        if self.habitat["primary"] == "Aquatic":
            if roll <= 0.3:
                self.habitat["sub"] = "Salt-Water"
            elif roll <= 0.9:
                self.habitat["sub"] = "Fresh Water"
            else:
                self.habitat["sub"] = "Brackish"

if __name__ == "__main__":
    # execute only if run as a script
    main()