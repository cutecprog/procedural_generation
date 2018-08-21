"""
Credits:
Tables (v1.1) by Sebastian Romu

"""
from random import random
from pprint import pprint

def main():
    flora = Flora()
    flora.generate()
    print("The flora is")
    print("{:>16}: ".format("Type") + flora.type)
    print("{:>16}: ".format("Habitat") + str(flora.habitat["primary"]))
    print("{:>16}: ".format("Sub-Habitat") + str(flora.habitat["sub"]))
    print("{:>16}: ".format("Grouping") + flora.grouping)
    print("{:>16}: ".format("Size") + flora.size)
    print("{:>16}: ".format("Main Body") + str(flora.body["main"]))
    print("{:>16}: ".format("Branches") + str(flora.body["branches"]))
    print("{:>16}: ".format("Roots") + str(flora.body["roots"]))
    print("{:>16}: ".format("Leaves / Cap") + str(flora.leaves))
    #print("{:>16}: ".format("Leaf Location") + str(flora.leaves["location"]))
    #pprint(vars(flora))

#----------------------- Globals ----------------------------------------------

gravity = 0     # Planetary Gravity Index
aura = 0        # Planetary Aura Index
table_names = ["type", "habitat", "grouping", "size", "body", "leaves", \
        "reproduction", "diet", "sentience", "edibility"]

#------------------------ Functions -------------------------------------------

def select(roll, table, allow_row_twice=True):
    for tag in sorted(table, key=table.get):
        # sort table able by weights
        if roll <= table[tag]:
            if allow_row_twice and tag == "Roll Twice":
                return roll_twice(table)
            return tag
    print("Error: No value less than or equal to " + roll)

def add_without_repeat(tag, additional_tag):
    if additional_tag != tag:
        # both rolled subhabitats aren't the same
        return [tag, additional_tag]
    return tag

def roll_twice(table):
    output = ["Roll Twice", "Roll Twice"]
    # Reroll if land on roll twice
    while output[0] == "Roll Twice":
        output[0] = select(random(), table, allow_row_twice=False)
    while output[1] == "Roll Twice" or output[1] == output[0]:
        output[1] = select(random(), table, allow_row_twice=False)
    return output

#------------------------------ Tables ----------------------------------------

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
branches_table = {"Woody":
        {"Radial": 0.55, "Ordered": 0.75, "Random": 0.99, "None": 1},
        "Herbaceous":
        {"Radial": 0.45, "Ordered": 0.50, "Random": 0.85, "None": 1},
        "Algae":
        {"Radial": 0.25, "Ordered": 0.60, "Random": 0.90, "None": 1},
        "Fungus":
        {"Radial": 0.02, "Ordered": 0.05, "Random": 0.15, "None": 1} }
# Table 5b
roots_table = {"Woody":
        {"Tap": 0.35, "Tubers": 0.37, "Fibrous": 0.84, "Advantageous": 0.93,
        "Bulb": 0.95, "Rhizoid": 0.99, "None": 1},
        "Herbaceous":
        {"Tap": 0.35, "Tubers": 0.45, "Fibrous": 0.73, "Advantageous": 0.77,
        "Bulb": 0.90, "Rhizoid": 0.99, "None": 1},
        "Algae":
        {"Tap": 0.01, "Tubers": 0.02, "Fibrous": 0.04, "Advantageous": 0.15,
        "Bulb": 0.19, "Rhizoid": 0.50, "None": 1},
        "Fungus":
        {"Tap": 0.03, "Tubers": 0.09, "Fibrous": 0.15, "Advantageous": 0.20,
        "Bulb": 0.30, "Rhizoid": 0.90, "None": 1} }
# Table 5c
body_surface_table = {"Woody":
        {"Smooth": 0.30, "Waxy": 0.40, "Rough": 0.70, "Scaly": 0.84,
        "Flaky": 0.97, "Other": 0.99, "Roll Twice": 1},
        "Herbaceous":
        {"Smooth": 0.59, "Waxy": 0.79, "Rough": 0.85, "Scaly": 0.90,
        "Flaky": 0.94, "Other": 0.99, "Roll Twice": 1},
        "Algae":
        {"Smooth": 0.65, "Waxy": 0.70, "Rough": 0.75, "Scaly": 0.82,
        "Flaky": 0.90, "Other": 0.99, "Roll Twice": 1} }
body_surface_table["Fungus"] = body_surface_table["Algae"]
# Table 5d
color_table = {"Red": 0.05, "Orange": 0.10, "Yellow": 0.20, "Green": 0.45,
        "Blue": 0.50, "Violet": 0.55, "Black": 0.60, "Grey": 0.65,
        "White": 0.70, "Brown": 0.80, "Silver": 0.85, "Copper": 0.90,
        "Gold": 0.95, "Roll Twice": 1}
pattern_table = {"Spotted": 0.10, "Mottled": 0.20, "Patches": 0.25,
        "Stripes": 0.25, "Solid": 0.60, "Phases": 0.75, "Translucent": 0.80,
        "Iridescent": 0.85, "Luminescent": 0.90, "Blushed": 0.95, "Roll Twice": 1}
# Table 6
leaves_table = {"Woody":
        {"Broad": 0.55, "Needles": 0.70, "Compound": 0.94, "Blades": 0.97,
        "Scales": 0.98, "Roll Twice": 0.99, "None": 1},
        "Herbaceous":
        {"Broad": 0.45, "Needles": 0.50, "Compound": 0.85, "Blades": 0.97,
        "Scales": 0.98, "Roll Twice": 0.99, "None": 1},
        "Algae":
        {"Broad": 0.02, "Needles": 0.03, "Compound": 0.10, "Blades": 0.11,
        "Scales": 0.15, "Roll Twice": 0.30, "None": 1},
        "Fungus":
        {"Broad": 0.25, "Needles": 0.50, "Compound": 0.60, "Blades": 0.80,
        "Scales": 0.90, "Roll Twice": 0.95, "None": 1} }
# Table 6a
leaf_location_table = {"Terminal": 0.30, "Branch Points": 0.50,
        "Random Interval": 0.70, "Regular Interval": 0.90,
        "Stem / Trunk": 0.98, "Roll Twice": 1}
# Table 6b
leaf_shape = {}

leaf_margin = {}
# Table 6c
# Table 6d
# Table 6e
#{"Woody":{},"Herbaceous":{},"Algae":{},"Fungus":{} }
test_table = {"Woody":{"Roll Twice": 1},"Herbaceous":{"Roll Twice": 1},
        "Algae":{"Roll Twice": 1},"Fungus":{"Roll Twice": 1}}

#----------------------- Classes ----------------------------------------------

class Flora(object):
    def __init__(self):
        self.type = ""
        self.habitat = {}
        self.grouping = ""
        self.size = ""
        self.body = {}
        self.leaves = {}
        self.reproduction = {}
        self.diet = {}
        self.sentience = {}
        self.edibility = {}

    def generate(self):
        # Table 1
        self.type = select(random(), type_table)
        # Table 2*
        self._generate_habitat()
        # Table 3
        self.grouping = select(random(), grouping_table[self.type])
        # Table 4
        self.size = select(random(), size_table[self.type])
        # Table 5*
        self._generate_body()
        # Table 6*
        self._generate_leaves()

    def _generate_habitat(self):
        # Table 2
        self.habitat["primary"] = select(random() - 5 * gravity, habitat_table[self.type])
        if self.habitat["primary"] == "Aquatic":
            # Table 2a
            self.habitat["sub"] = select(random(), subhabitat_table["Aquatic"])
        else:
            # Table 2b
            self.habitat["sub"] = select(random(), subhabitat_table["Other"])
            if random() <= 0.10:
                # 10% chance of two subhabitats
                self.habitat["sub"] = add_without_repeat(self.habitat["sub"], \
                        select(random(), subhabitat_table["Other"]))
        # Table 2c
        if type(self.habitat["sub"]) is list:
            self.habitat["sub"] = [
                    [self.habitat["sub"][0], select(random(), rarity_table)],
                    [self.habitat["sub"][1], select(random(), rarity_table)] ]
        else:
            self.habitat["sub"] = \
                    [self.habitat["sub"], select(random(), rarity_table)]

    def _generate_body(self):
        # Table 5
        self.body["main"] = select(random(), body_table[self.type])
        # Table 5a
        self.body["branches"] = select(random(), branches_table[self.type])
        # Table 5b
        self.body["roots"] = select(random(), roots_table[self.type])
        # Table 5c
        if self.body["main"] is list:
            self.body["main"] = [ {"type": self.body["main"][0],
                    "surface": select(random(), body_surface_table[self.type]) },
                    {"type": self.body["main"][1],
                    "surface": select(random(), body_surface_table[self.type]) } ]
        else:
            self.body["main"] = {"type": self.body["main"], \
                    "surface": select(random(), body_surface_table[self.type])}
        if self.body["branches"] != "None":
            self.body["branches"] = {"type": self.body["branches"], \
                    "surface": select(random(), body_surface_table[self.type])}
        if self.body["roots"] != "None":
            self.body["roots"] = {"type": self.body["roots"], \
                    "surface": select(random(), body_surface_table[self.type])}
        # Table 5d
        if self.body["main"] is list:
            # Is 2d list
            self.body["main"][0]["color"] = select(random(), color_table)
            self.body["main"][1]["color"] = select(random(), color_table)
            self.body["main"][0]["pattern"] = select(random(), pattern_table)
            self.body["main"][1]["pattern"] = select(random(), pattern_table)
        else:
            self.body["main"]["color"] = select(random(), color_table)
            self.body["main"]["pattern"] = select(random(), pattern_table)
        if self.body["branches"] != "None":
            self.body["branches"]["color"] = select(random(), color_table) 
            self.body["branches"]["pattern"] = select(random(), pattern_table) 

        if self.body["roots"] != "None":
            self.body["roots"]["color"] = select(random(), color_table) 
            self.body["roots"]["pattern"] = select(random(), pattern_table) 

    def _generate_leaves(self):
        self.leaves["type"] = select(random(), leaves_table[self.type])
        if self.leaves["type"] == "None":
            return
        # Table 6a
        if self.type == "Fungus":
            self.leaves["location"] = "Terminal"
        else:
            self.leaves["location"] = select(random(), leaf_location_table)
        # Table 6b

if __name__ == "__main__":
    # execute only if run as a script
    main()