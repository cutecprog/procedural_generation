from random import randint, random, shuffle

def main():
        print("Gear tags are")
        print(randharm())
        print(randrange())

        shuffle(tags)
        for n in [1.0, 0.85, 0.42, 0.4, 0.4, 0.4]:
                if random() <= n:
                        print(tags.pop())
                else:
                        break

def randharm():
        return "Harm " + str(randint(1,3))

def randrange():
        return ["Hand", "Close", "Far"][randint(0,2)]

tags = ["automatic", "area", "balanced", "fire", "healing", "heavy", "holy", \
                "ignore-armour", "innocuous", "intimate", "loud", "magic", \
                "many", "[a material]", "messy", "quick", "reload", "slow", \
                "small", "unreliable", "useful", "valuable", "volatile"]

if __name__ == "__main__":
        # execute only if run as a script
        main()
