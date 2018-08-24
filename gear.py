from random import randint, random, shuffle

def main():
        print("Gear tags are")
        print(randharm())
        print(randrange())

        if random() <= 0.15:
                print("magic")

        shuffle(tags)
        for n in [1.0, 0.85, 0.42, 0.4, 0.4, 0.4]:
                if random() > n:
                        break

                tag = tags.pop()
                if tag == "automatic":
                        # Automatic tag 90% has reload tag
                        if random() <= 0.7 and "reload" in tags:
                                tags.remove("reload")
                                print("reload")
                elif tag == "quick":
                        tags.remove("slow")
                elif tag == "slow":
                        tags.remove("quick")
                elif tag == "[a material]":
                        shuffle(materials)
                        tag = materials.pop()
                print(tag)

def randharm():
        return "harm " + str(randint(1,3))

def randrange():
        range_tag = ["intimate", "hand", "close", "far"][randint(0,3)]
        if range_tag == "far" and random() <= 0.70:
            tags.remove("reload")
            return "far\nreload"
        return range_tag

tags = ["automatic", "area", "balanced", "fire", "healing", "heavy", "holy", \
                "ignore-armour", "innocuous", "loud", \
                "many", "[a material]", "messy", "quick", "reload", "slow", \
                "small", "unreliable", "useful", "valuable", "volatile"]

materials = ["wood", "silver alloy", "copper alloy", "iron alloy", \
                "polycarbon", "bone"]

if __name__ == "__main__":
        # execute only if run as a script
        main()