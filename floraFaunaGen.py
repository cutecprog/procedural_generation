"""
Tables by Sebastian Romu

"""

def main():
        print("The flora is")
        for name in table_names:
                print("{:>12}: ".format(name))
        

gravity = 0     # Planetary Gravity Index
aura = 0        # Planetary Aura Index
table_names = ["Type", "Habitat", "Grouping", "Size", "Body", "Leaves", \
                "Reproduction", "Diet", "Sentience", "Edibility"]

if __name__ == "__main__":
        # execute only if run as a script
        main()