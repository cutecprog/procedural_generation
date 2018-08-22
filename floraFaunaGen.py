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
    '''print("{:>16}: ".format("Type") + flora.type)
    print("{:>16}: ".format("Habitat") + str(flora.habitat["primary"]))
    print("{:>16}: ".format("Sub-Habitat") + str(flora.habitat["sub"]))
    print("{:>16}: ".format("Grouping") + flora.grouping)
    print("{:>16}: ".format("Size") + flora.size)
    print("{:>16}: ".format("Main Body") + str(flora.body["main"]))
    print("{:>16}: ".format("Branches") + str(flora.body["branches"]))
    print("{:>16}: ".format("Roots") + str(flora.body["roots"]))
    print("{:>16}: ".format("Leaves / Cap") + str(flora.leaves))'''
    pprint(vars(flora))

#----------------------- Globals ----------------------------------------------

gravity = 0     # Planetary Gravity Index
aura = 0        # Planetary Aura Index
table_names = ["type", "habitat", "grouping", "size", "body", "leaves", \
        "reproduction", "diet", "sentience", "edibility"]

#------------------------ Functions -------------------------------------------

def select(table, modifier = 0, allow_row_twice = True):
    roll = random() + modifier
    for tag in sorted(table, key=table.get):
        # sort table able by weights
        if roll <= table[tag]:
            if allow_row_twice and tag == "Roll Twice":
                return roll_twice(table, modifier)
            return tag
    print("Error: No value less than or equal to " + roll)

def add_without_repeat(tag, additional_tag):
    if additional_tag != tag:
        # both rolled subhabitats aren't the same
        return [tag, additional_tag]
    return tag

def roll_twice(table, modifier = 0):
    output = ["Roll Twice", "Roll Twice"]
    # Reroll if land on roll twice
    while output[0] == "Roll Twice":
        output[0] = select(table, allow_row_twice=False)
    while output[1] == "Roll Twice" or output[1] == output[0]:
        output[1] = select(table, allow_row_twice=False)
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
# Table 5d and 6e
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
leaf_shape_table = {"Acicular": 0.03, "Subulate": 0.06, "Lanceolate": 0.10,
        "Linear": 0.14, "Falcate": 0.17, "Spear-Shaped": 0.21, "Hastate": 0.25,
        "Deltoid": 0.28, "Rhomboid": 0.32, "Cuneate": 0.35, "Cordate": 0.39,
        "Obcordate": 0.43, "Ovate": 0.47, "Obovate": 0.51, "Acuminate": 0.56,
        "Aristate": 0.58, "Orbicular": 0.61, "Obtuse": 0.64, "Elliptic": 0.67,
        "Reniform": 0.70, "Spatulate": 0.72, "Truncate": 0.75,
        "Flabellate": 0.78, "Lobed": 0.81, "Pinnatisect": 0.83,
        "Poly-Foliate": 0.87, "Palmate": 0.92, "Pedate": 0.96, "Digitate": 0.98,
        "Roll Twice": 1}

leaf_margin_table = {"Smooth": 0.15, "Sinuate": 0.30, "Undulate": 0.40, "Spiny": 0.45,
        "Lobate": 0.55, "Crenate": 0.60, "Dentate": 0.70, "Denticulate": 0.75,
        "Serate": 0.85, "Serrulate": 0.90, "Ciliate": 0.95, "Roll Twice": 1}
# Table 6c
leaf_surface_table = {"Smooth": 0.25, "Waxy": 0.40, "Scaly": 0.55, "Hairy": 0.65,
        "Velvety": 0.80, "Dusty": 0.90, "Sticky": 0.96, "Roll Twice": 1}
# Table 6d
leaf_venation_table = {"Arcuate": 0.10, "Cross-Venulate": 0.20,
        "Dichotomous": 0.30, "Longitudinal": 0.45, "Palmate": 0.60,
        "Parallel": 0.70, "Pinnate": 0.80, "Reticulate": 0.90, "None": 0.99,
        "Roll Twice": 1 }
leaf_numbers_table = {"Single": 0.20, "Pairs": 0.40, "Whorls": 0.60,
        "Clusters": 0.95, "Roll Twice": 1}
# Table 7
reproduction_table = {"Woody":
        {"Seeds": 0.80, "Suckers": 0.92, "Budding / Fragmentation": 0.98,
        "Other": 0.99, "Roll Twice": 1},
        "Herbaceous":
        {"Seeds": 0.63, "Suckers": 0.85, "Budding / Fragmentation": 0.98,
        "Other": 0.99, "Roll Twice": 1},
        "Algae":
        {"Seeds": 0.02, "Suckers": 0.06, "Budding / Fragmentation": 0.90,
        "Other": 0.99, "Roll Twice": 1},
        "Fungus":
        {"Seeds": 0.89, "Suckers": 0.95, "Budding / Fragmentation": 0.98,
        "Other": 0.99, "Roll Twice": 1} }
# Table 7a
seeds_table = {"Woody":
        {"Grain": 0.05, "Nut": 0.50, "Fruit": 0.94, "Spore": 0.99, "Other": 1},
        "Herbaceous":
        {"Grain": 0.40, "Nut": 0.45, "Fruit": 0.80, "Spore": 0.99, "Other": 1},
        "Algae":
        {"Grain": 0.02, "Nut": 0.04, "Fruit": 0.06, "Spore": 0.90, "Other": 1} }
seeds_table["Fungus"] = seeds_table["Algae"]
# Table 7b (This table is incomplete)
seed_dispersal_table = {"Grain":
        {"Animal": 0.20, "Wind": 0.40, "Water": 0.60, "Gravity": 0.98, "Other": 1},
        "Nut":
        {"Animal": 0.45, "Wind": 0.53, "Water": 0.60, "Gravity": 0.98, "Other": 1},
        "Fruit":
        {"Animal": 0.60, "Wind": 0.65, "Water": 0.85, "Gravity": 0.98, "Other": 1},
        "Spore":
        {"Animal": 0.40, "Wind": 0.83, "Water": 0.90, "Gravity": 0.98, "Other": 1},
        "Other": {"Other": 1} # Missing is source doc
        }
# Table 7c
flower_table = {"Grain":
        {"None": 0.02, "Single": 0.05, "Pairs": 0.10, "Bunches": 0.30,
        "Compound": 0.50, "Spray": 0.90, "Other": 1},
        "Nut":
        {"None": 0.02, "Single": 0.40, "Pairs": 0.60, "Bunches": 0.80,
        "Compound": 0.90, "Spray": 0.95, "Other": 1},
        "Fruit":
        {"None": 0.03, "Single": 0.30, "Pairs": 0.60, "Bunches": 0.70,
        "Compound": 0.80, "Spray": 0.90, "Other": 1},
        "Spore":
        {"None": 0.40, "Single": 0.50, "Pairs": 0.60, "Bunches": 0.70,
        "Compound": 0.80, "Spray": 0.90, "Other": 1},
        "Other":
        {"None": 0.10, "Single": 0.20, "Pairs": 0.30, "Bunches": 0.50,
        "Compound": 0.70, "Spray": 0.90, "Other": 1} }
# Table 7d
# Table 7e
# Table 7f
# Table 7g
# Table 7h
# Table 7i
# Table 7j
# Table 7k
# Table 7l
# Table 8 (change made: Re-roll twice removed 'Re-roll Twice' keep 'Other')
diet_table = {"Woody":
        {"Photo/Chemo-synthetic": 0.89, "Predaceous": 0.90, "Decay": 0.95,
        "Parasitic": 0.98, "Symbiotic": 0.99, "Other": 1},
        "Herbaceous":
        {"Photo/Chemo-synthetic": 0.85, "Predaceous": 0.87, "Decay": 0.93,
        "Parasitic": 0.96, "Symbiotic": 0.98, "Other": 1},
        "Algae":
        {"Photo/Chemo-synthetic": 0.92, "Predaceous": 0.93, "Decay": 0.94,
        "Parasitic": 0.95, "Symbiotic": 0.99, "Other": 1},
        "Fungus":
        {"Photo/Chemo-synthetic": 0.05, "Predaceous": 0.08, "Decay": 0.90,
        "Parasitic": 0.94, "Symbiotic": 0.98, "Other": 1}
        # Change made above to ^^^^ 0.99 to 0.98
        }
# Table 8a
tropism_table = {"Woody":
        {"None": 0.02, "Gravity": 0.55, "Light": 0.83, "Heat": 0.87,
        "Touch": 0.97, "Motile": 0.98, "Mobile": 0.99, "Roll Twice": 1},
        "Herbaceous":
        {"None": 0.05, "Gravity": 0.40, "Light": 0.82, "Heat": 0.87,
        "Touch": 0.97, "Motile": 0.98, "Mobile": 0.99, "Roll Twice": 1},
        "Algae":
        {"None": 0.20, "Gravity": 0.35, "Light": 0.60, "Heat": 0.85,
        "Touch": 0.90, "Motile": 0.94, "Mobile": 0.98, "Roll Twice": 1},
        "Fungus":
        {"None": 0.30, "Gravity": 0.70, "Light": 0.80, "Heat": 0.90,
        "Touch": 0.96, "Motile": 0.98, "Mobile": 0.99, "Roll Twice": 1} }
# Table 9
sentience_chance = {"Photo/Chemo-synthetic": 0.99, "Predaceous": 0.97,
        "Decay": 0.99, "Parasitic": 0.98, "Symbiotic": 0.98, "Other": 0.97 }
# Table 9a
sentience_table = {"Instinctual": 0.75, "Hive": 0.79, "Animal": 0.89,
        "Cunning Animal": 0.99, "Sapient": 1}
# Table 10
# Table 10a
# Table 10b
# Table 10c
#{"Grain":{},"Nut":{},"Fruit":{},"Spore":{},"Other":{} }
#{"Woody":{},"Herbaceous":{},"Algae":{},"Fungus":{} }

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
        self.sentience = ""
        self.edibility = {}

    def generate(self):
        # Table 1
        self.type = select(type_table)
        # Table 2*
        self._generate_habitat()
        # Table 3
        self.grouping = select(grouping_table[self.type])
        # Table 4
        self.size = select(size_table[self.type])
        # Table 5*
        self._generate_body()
        # Table 6*
        self._generate_leaves()
        # Table 7*
        self._generate_reproduction()
        # Table 8
        self.diet["type"] = select(diet_table[self.type])
        # Table 8a
        self.diet["tropism"] = select(tropism_table[self.type])
        # Table 9*
        self._generate_sentience()

    def _generate_habitat(self):
        # Table 2
        self.habitat["primary"] = select(habitat_table[self.type], -0.05 * gravity)
        # Table 2a, 2b
        self.habitat["sub"] = {}
        if self.habitat["primary"] == "Aquatic":
            # Table 2a
            self.habitat["sub"]["type"] = select(subhabitat_table["Aquatic"])
        else:
            # Table 2b
            if random() <= 0.10:
                # 10% chance of two subhabitats
                self.habitat["sub"] = roll_twice(subhabitat_table["Other"])
                self.habitat["sub"][0] = {"type": self.habitat["sub"][0]}
                self.habitat["sub"][1] = {"type": self.habitat["sub"][1]}
            else:
                self.habitat["sub"]["type"] = select(\
                        subhabitat_table["Other"])
        # Table 2c
        if type(self.habitat["sub"]) is list:
            self.habitat["sub"][0]["rarity"] = select(rarity_table)
            self.habitat["sub"][1]["rarity"] = select(rarity_table)
        else:
            self.habitat["sub"]["rarity"] = select(rarity_table)

    def _generate_body(self):
        # Table 5
        self.body["main"] = select(body_table[self.type])
        # Table 5a
        self.body["branches"] = select(branches_table[self.type])
        # Table 5b
        self.body["roots"] = select(roots_table[self.type])
        # Table 5c
        self.body["main"] = {"type": self.body["main"], \
                    "surface": select(body_surface_table[self.type])}
        if self.body["branches"] != "None":
            self.body["branches"] = {"type": self.body["branches"], \
                    "surface": select(body_surface_table[self.type])}
        if self.body["roots"] != "None":
            self.body["roots"] = {"type": self.body["roots"], \
                    "surface": select(body_surface_table[self.type])}
        # Table 5d
        self.body["main"]["color"] = select(color_table)
        self.body["main"]["pattern"] = select(pattern_table)
        if self.body["branches"] != "None":
            self.body["branches"]["color"] = select(color_table) 
            self.body["branches"]["pattern"] = select(pattern_table) 

        if self.body["roots"] != "None":
            self.body["roots"]["color"] = select(color_table) 
            self.body["roots"]["pattern"] = select(pattern_table) 

    def _generate_leaves(self):
        # Table 6
        self.leaves["type"] = select(leaves_table[self.type])
        if type(self.leaves["type"]) is list:
            self.leaves = [{"type": self.leaves["type"][0]}, \
                    {"type": self.leaves["type"][1]} ]
        elif self.leaves["type"] == "None":
            return
        # Tables 6a+
        if type(self.leaves) is list:
            self.leaves[0] = self.__get_random_leaf_of_type(self.leaves[0]["type"])
            self.leaves[1] = self.__get_random_leaf_of_type(self.leaves[1]["type"])
        else:
            self.leaves = self.__get_random_leaf_of_type(self.leaves["type"])

    def __get_random_leaf_of_type(self, type):
        leaf = {"type": type}
        # Table 6a
        if self.type == "Fungus":
            leaf["location"] = "Terminal"
        else:
            leaf["location"] = select(leaf_location_table)
        # Table 6b
        leaf["shape"] = select(leaf_shape_table)
        leaf["margin"] = select(leaf_margin_table)
        # Table 6c
        leaf["surface_topside"] = select(leaf_surface_table)
        leaf["surface_underside"] = select(leaf_surface_table)
        # Table 6d
        leaf["venation"] = select(leaf_venation_table)
        leaf["numbers"] = select(leaf_numbers_table)
        leaf["color"] = select(color_table)
        leaf["pattern"] = select(pattern_table)
        return leaf

    def _generate_reproduction(self):
        # Table 7
        self.reproduction["type"] = select(reproduction_table[self.type])
        if "Seeds" not in self.reproduction["type"]:
            return
        # Table 7a
        self.reproduction["seed_type"] = select(seeds_table[self.type])
        # Table 7b
        self.reproduction["seed_dispersal"] = \
                select(seed_dispersal_table[self.reproduction["seed_type"]])
        # Table 7c
        self.reproduction["flower_type"] = \
                select(flower_table[self.reproduction["seed_type"]])
        if self.reproduction["flower_type"] == "None":
            return

    def _generate_sentience(self):
        roll = random() + aura * 0.05
        if self.diet["tropism"] == "Motile":
            roll += 0.10
        elif self.diet["tropism"] == "Mobile":
            roll += 0.20
        if roll <= sentience_chance[self.diet["type"]]:
            self.sentience = "Non-Sentient"
        else:
            modifier = 0.05 * aura
            if self.diet["type"] == "Symbiotic":
                modifier += 0.05
            elif self.diet["type"] == "Predaceous":
                modifier += 0.10
            self.sentience = select(sentience_table, modifier)
            if self.sentience == "Hive":
                self.sentience = [self.sentience, select(sentience_table, modifier)]

if __name__ == "__main__":
    # execute only if run as a script
    main()