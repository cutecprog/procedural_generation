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

type_table = {"Woody": 0.30, "Herbaceous": 0.85, "Algae": 0.90, "Fungus": 1}

habitat_table = {"Woody": \
        {"Aquatic": 0.05, "Sub-Terrestrial": 0.10, "Terrestrial": 0.99, "Avian": 1}, \
        "Herbaceous": \
        {"Aquatic": 0.35, "Sub-Terrestrial": 0.40, "Terrestrial": 0.99, "Avian": 1}, \
        "Algae": \
        {"Aquatic": 0.80, "Sub-Terrestrial": 0.90, "Terrestrial": 0.98, "Avian": 1}, \
        "Fungus": \
        {"Aquatic": 0.10, "Sub-Terrestrial": 0.40, "Terrestrial": 0.99, "Avian": 1} }

subhabitat_table = {"Aquatic": \
        {"Salt-Water": 0.30, "Fresh Water": 0.90, "Brackish": 1}, \
        "Other": \
        {"Desert / Waste": 0.10, "Plains / Savannah": 0.40, \
        "Marsh / Swamp / Bog": 0.50, "Forest / Jungle": 0.80, \
        "Hills / Scrub": 0.90, "Mountains": 0.95, "Tundra": 1} }

class Flora(object):
    def __init__(self):
        self.type = select(random(), type_table)
        self.habitat = {}
        self.habitat["primary"] = select(random() - 5 * gravity, habitat_table[self.type])
        if self.habitat["primary"] == "Aquatic":
            self.habitat["sub"] =  select(random(), subhabitat_table["Aquatic"])
        else:
            self.habitat["sub"] =  select(random(), subhabitat_table["Other"])

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