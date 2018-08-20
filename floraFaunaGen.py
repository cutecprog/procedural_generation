"""
Tables by Sebastian Romu

"""
from random import random

def main():
    print("The flora is")
    print(vars(flora()))
    for name in table_names:
        print("{:>12}: ".format(name))
        

gravity = 0     # Planetary Gravity Index
aura = 0        # Planetary Aura Index
table_names = ["Type", "Habitat", "Grouping", "Size", "Body", "Leaves", \
                "Reproduction", "Diet", "Sentience", "Edibility"]

class flora(object):
    def __init__(self):
        self.type = ""
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