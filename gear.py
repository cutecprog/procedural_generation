from random import randint, random

def main():
        print("Gear tags are")
        print(randharm())
        print(randrange())

        for n in [1.0, 0.85, 0.42, 0.4, 0.4, 0.4]:
                if random() <= n:
                        print("tag")
                else:
                        break

def randharm():
        return "Harm " + str(randint(1,3))

def randrange():
        return ["Hand", "Close", "Far"][randint(0,2)]

if __name__ == "__main__":
        # execute only if run as a script
        main()
