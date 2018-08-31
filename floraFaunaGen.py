"""
Credits:
Random Flora Tables v1.1 by Sebastian Romu
https://entorais.wordpress.com/2016/08/02/random-plants/

"""
from random import random, randint
from flora_tables import *

def main():
    flora = Flora()
    flora.generate()
    print("The flora is")
    pprint(vars(flora))

#----------------------- Globals ----------------------------------------------

gravity = 0     # Planetary Gravity Index
aura = 0        # Planetary Aura Index

#------------------------ Functions -------------------------------------------

def select(table, modifier = 0, allow_row_twice = True):
    roll = random() + modifier
    if roll > 1.0:
        roll = 1.0
    for tag in sorted(table, key=table.get):
        # sort table able by weights
        if roll <= table[tag]:
            if allow_row_twice and tag == "Roll Twice":
                return roll_twice(table, modifier)
            return tag
    print("Error: No value less than or equal to " + str(roll))

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

def account_for_two(tag, generate):
    #self.leaves["type"] = select(leaves_table[self.type])
    if type(tag["type"]) is list:
        tag = [{"type": tag["type"][0]}, {"type": tag["type"][1]} ]
    elif tag["type"] == "None":
        return
    if type(tag) is list:
        tag[0] = generate(tag[0]["type"])
        tag[1] = generate(tag[1]["type"])
    else:
        tag = generate(tag["type"])
    return tag

def roll_dice(roll):
    if roll == "None":
        return 0
    # Remove all whitespace
    roll = "".join(roll.split())
    sum = 0
    for n in roll.split("+"):
        arg = n.split('d')
        if len(arg) == 1:
            sum += int(arg[0])
        elif len(arg) == 2:
            number_of_rolls = int(arg[0])
            die_type = int(arg[1])
            for i in range(0, number_of_rolls):
                sum += randint(1, die_type)
    return sum

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
        # Table 10*
        self._generate_edibility()

    def _generate_habitat(self):
        # Table 2
        self.habitat["primary"] = \
                select(habitat_table[self.type], -0.05 * gravity)
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
        # Table 6a+
        self.leaves = account_for_two(self.leaves, self.__get_random_leaf_of_type)

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
        # Table 7d
        self.reproduction["flower_shape"] = select(
                flower_shape_table[self.reproduction["flower_type"]] )
        # Table 7e
        self.reproduction["flower_size"] = select(flower_size_table)
        # Table 7f
        self.reproduction["petal_number"] = \
                roll_dice(select(petal_number_table))
        if self.reproduction["petal_number"] > 0:
            self.reproduction["petal_shape"] = select(petal_shape_table)
            # Table 7g
            self.reproduction["petal_surface_inside"] = \
                    select(petal_surface_table)
            self.reproduction["petal_surface_outside"] = \
                    select(petal_surface_table)
        # Table 7h
        self.reproduction["flower_location"] = select(flower_location_table)
        # Table 7i
        self.reproduction["flower_scent"] = select(flower_scent_table)
        # Table 7j
        modifier = 0
        if self.type == "Woody":
            modifier = 0.15
        self.reproduction["flower_frequency"] = \
                select(flower_frequency_table, modifier)
        # Table 7k
        self.reproduction["flower_color"] = select(flower_color_table)
        # Table 7l
        self.reproduction["flower_stamens"] = select(flower_stamens_table)
        self.reproduction["flower_pistils"] = select(flower_pistils_table)

    def _generate_sentience(self):
        # Table 9
        roll = random() + 0.05 * aura
        if self.diet["tropism"] == "Motile":
            roll += 0.10
        elif self.diet["tropism"] == "Mobile":
            roll += 0.20
        if roll <= sentience_chance[self.diet["type"]]:
            self.sentience = "Non-Sentient"
            return
        # Table 9a
        modifier = 0.05 * aura
        if self.diet["type"] == "Symbiotic":
            modifier += 0.05
        elif self.diet["type"] == "Predaceous":
            modifier += 0.10
        self.sentience = select(sentience_table, modifier)
        if self.sentience == "Hive":
            self.sentience = [self.sentience, select(sentience_table, modifier)]

    def _generate_edibility(self):
        # Table 10
        self.edibility["type"] = select(edibility_table[self.type])
        # Table 10a+
        self.edibility = account_for_two(self.edibility,
                self.__get_random_use_of_type)
    
    def __get_random_use_of_type(self, type):
        # Table 10a
        use = {"type": type}
        if type == "Edible" or type == "Nutritious / Tasty":
            use["preparation"] = \
                    select(edible_preparation_table[type])
        # Table 10b+
        if type == "Medicinal":
            # Table 10b
            use["property"] = select(medicinal_properties_table)
            # Table 10c
            use["preparation"] = select(medicinal_preparation_table)
        return use

if __name__ == "__main__":
    # execute only if run as a script
    from pprint import pprint
    main()