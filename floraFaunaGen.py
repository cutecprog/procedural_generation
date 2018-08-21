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

def select(roll, weights):
    for tag in sorted(weights, key=weights.get):
        # sort table able by weights
        if roll <= weights[tag]:
            return tag
    print("Error: No value less than or equal to " + roll)

def roll_twice(tag, additional_tag):
    if additional_tag != tag:
        # both rolled subhabitats aren't the same
        return [tag, additional_tag]
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

rarity_table = {"Very Common": 0.15, "Common": 0.50, "Uncommon": 0.80, \
        "Rare": 0.94, "Very Rare": 0.99, "Unique": 1}

class Flora(object):
    def __init__(self):
        # Table 1
        self.type = select(random(), type_table)
        # Table 2
        self.habitat = {}
        self.habitat["primary"] = select(random() - 5 * gravity, habitat_table[self.type])
        if self.habitat["primary"] == "Aquatic":
            # Table 2a
            self.habitat["sub"] = select(random(), subhabitat_table["Aquatic"])
        else:
            # Table 2b
            self.habitat["sub"] = select(random(), subhabitat_table["Other"])
            if random() <= 0.10:
                # 10% chance of two subhabitats
                self.habitat["sub"] = roll_twice(self.habitat["sub"], \
                        select(random(), subhabitat_table["Other"]))
        #table 2c
        if type(self.habitat["sub"]) is list:
            pass
        else:
            self.habitat["sub"] = \
                    {self.habitat["sub"]: select(random(), rarity_table)}
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