"""
Tables by Sebastian Romu

"""
from random import random
from pprint import pprint

def main():
    flora = Flora()
    print("The flora is")
    print("{:>12}: ".format("Type") + flora.type)
    print("{:>12}: ".format("Habitat") + flora.habitat["primary"])
    print("{:>12}: ".format("Grouping") + flora.grouping)
    print("{:>12}: ".format("Size") + flora.size)
    pprint(vars(flora))

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
# Table 1
type_table = {"Woody": 0.30, "Herbaceous": 0.85, "Algae": 0.90, "Fungus": 1}
# Table 2
habitat_table = {"Woody":
        {"Aquatic": 0.05, "Sub-Terrestrial": 0.10, "Terrestrial": 0.99, "Avian": 1},
        "Herbaceous":
        {"Aquatic": 0.35, "Sub-Terrestrial": 0.40, "Terrestrial": 0.99, "Avian": 1},
        "Algae":
        {"Aquatic": 0.80, "Sub-Terrestrial": 0.90, "Terrestrial": 0.98, "Avian": 1},
        "Fungus":
        {"Aquatic": 0.10, "Sub-Terrestrial": 0.40, "Terrestrial": 0.99, "Avian": 1} }
# Table 2a, 2b
subhabitat_table = {"Aquatic":
        {"Salt-Water": 0.30, "Fresh Water": 0.90, "Brackish": 1},
        "Other":
        {"Desert / Waste": 0.10, "Plains / Savannah": 0.40,
        "Marsh / Swamp / Bog": 0.50, "Forest / Jungle": 0.80,
        "Hills / Scrub": 0.90, "Mountains": 0.95, "Tundra": 1} }
# Table 2c
rarity_table = {"Very Common": 0.15, "Common": 0.50, "Uncommon": 0.80,
        "Rare": 0.94, "Very Rare": 0.99, "Unique": 1}
# Table 3
grouping_table = {"Woody":
        {"Solitary": 0.20, "Small Patch": 0.40, "Medium Patch": 0.80, "Large Patch": 1},
        "Herbaceous":
        {"Solitary": 0.30, "Small Patch": 0.50, "Medium Patch": 0.90, "Large Patch": 1},
        "Algae":
        {"Solitary": 0.25, "Small Patch": 0.70, "Medium Patch": 0.95, "Large Patch": 1} }
grouping_table["Fungus"] = grouping_table["Algae"]
# Table 4
size_table = {"Woody":
        {"Huge": 0.15, "Large": 0.45, "Average": 0.80, "Small": 0.98, "Tiny": 1},
        "Herbaceous":
        {"Huge": 0.10, "Large": 0.20, "Average": 0.70, "Small": 0.95, "Tiny": 1},
        "Algae":
        {"Huge": 0.02, "Large": 0.15, "Average": 0.65, "Small": 0.85, "Tiny": 1},
        "Fungus":
        {"Huge": 0.01, "Large": 0.10, "Average": 0.30, "Small": 0.60, "Tiny": 1} }
# Table 5
body_table = {"Woody":
        {"Colonial Mass": 0.02, "Creeper / Vine": 0.20, "Stem / Trunk": 0.70, 
        "Multiple Stems / Trunks": 0.99, "Roll Twice": 1},
        "Herbaceous":
        {"Colonial Mass": 0.03, "Creeper / Vine": 0.35, "Stem / Trunk": 0.70, 
        "Multiple Stems / Trunks": 0.98, "Roll Twice": 1},
        "Algae":
        {"Colonial Mass": 0.70, "Creeper / Vine": 0.75, "Stem / Trunk": 0.85, 
        "Multiple Stems / Trunks": 0.99, "Roll Twice": 1},
        "Fungus":
        {"Colonial Mass": 0.20, "Creeper / Vine": 0.40, "Stem / Trunk": 0.70, 
        "Multiple Stems / Trunks": 0.99, "Roll Twice": 1} }
# Table 5a
# Table 5b
# Table 5c
# Table 5d
# Table 6
# Table 6a
# Table 6b
# Table 6c
# Table 6d
# Table 6e
#{"Woody":{},"Herbaceous":{},"Algae":{},"Fungus":{}}

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
        # Table 2c
        if type(self.habitat["sub"]) is list:
            self.habitat["sub"] = [
                    {self.habitat["sub"][0]: select(random(), rarity_table)},
                    {self.habitat["sub"][1]: select(random(), rarity_table)}]
        else:
            self.habitat["sub"] = \
                    {self.habitat["sub"]: select(random(), rarity_table)}
        # Table 3
        self.grouping = select(random(), grouping_table[self.type])
        # Table 4
        self.size = select(random(), size_table[self.type])
        self.body = {}
        self.body["main"] = select(random(), body_table[self.type])
        self.leaves = {}
        self.reproduction = {}
        self.diet = {}
        self.sentience = {}
        self.edibility = {}

if __name__ == "__main__":
    # execute only if run as a script
    main()