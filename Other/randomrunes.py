# Adam Kvant
# Try set() for multiple champs in different lanes on combination
import random 
class Champions:
    def __init__(self):
        self.champlist = []
        self.top = ["Aatrox", "Camille", "Cho'Gath", "Darius", "Dr. Mundo", "Fiora", "Gangplank", "Garen", "Gnar", "Gwen", "Illaoi", "Irelia", "Jax", "Jayce",
                    "Kayle", "Kennen", "Kled", "Malphite", "Mordekaiser", "Nasus", "Ornn", "Pantheon", "Poppy", "Quinn", "Renekton", "Riven", "Rumble", "Sett",
                    "Shen", "Singed", "Sion", "Tahm Kench", "Teemo", "Tryndamere", "Urgot", "Volibear", "Wukong", "Yorick"]
        self.jg = ["Amumu", "Elise", "Evelynn", "Fiddlesticks", "Gragas", "Graves", "Hecarim", "Ivern", "Jarvan IV", "Karthus", "Kayn", "Kha'Zix", "Kindred",
                   "Lee Sin", "Lillia", "Master Yi", "Nidalee", "Nocturne", "Nunu & Willump", "Olaf", "Rammus", "Rek'Sai", "Rengar", "Sejuani", "Shaco", "Shyvana",
                   "Skarner", "Taliyah", "Trundle", "Udyr", "Vi", "Viego", "Warwick", "Xin Zhao", "Zac"]
        self.mid = ["Ahri", "Akali", "Akshan", "Anivia", "Annie", "Aurelion Sol", "Azir", "Cassiopeia", "Corki", "Diana", "Ekko", "Fizz", "Galio", "Heimerdinger",
                    "Kassadin", "Katarina", "Leblanc", "Lissandra", "Malzahar", "Neeko", "Orianna", "Qiyana", "Ryze", "Sylas", "Syndra", "Talon", "Twisted Fate",
                    "Veigar", "Vel'Koz", "Vex", "Viktor", "Vladimir", "Xerath", "Yasuo", "Yone", "Zed", "Ziggs", "Zoe"]
        self.bot = ["Aphelios", "Ashe", "Caitlyn", "Draven", "Ezreal", "Jhin", "Jinx", "Kai'Sa", "Kalista", "Kog'Maw", "Lucian", "Miss Fortune", "Samira", "Senna",
                    "Sivir", "Tristana", "Twitch", "Varus", "Vayne", "Xayah", "Zeri"]
        self.sup = ["Alistar", "Bard", "Blitzcrank", "Brand", "Braum", "Janna", "Karma", "Leona", "Lulu", "Lux", "Maokai", "Morgana", "Nami", "Nautilus", "Pyke",
                    "Rakan", "Rell", "Renata Glasc", "Seraphine", "Sona", "Soraka", "Swain", "Taric", "Thresh", "Yuumi", "Zilean", "Zyra"]
        random.shuffle(self.top)
        random.shuffle(self.jg)
        random.shuffle(self.mid)
        random.shuffle(self.bot)
        random.shuffle(self.sup)
        self.allchamps = []
        for champ in self.top:
            self.allchamps.append(champ)
        for champ in self.jg:
            self.allchamps.append(champ)
        for champ in self.mid:
            self.allchamps.append(champ)
        for champ in self.bot:
            self.allchamps.append(champ)
        for champ in self.sup:
            self.allchamps.append(champ)
        random.shuffle(self.allchamps)
    def TotalChamps(self):
        print(len(self.top) + len(self.jg) + len(self.mid) + len(self.bot) + len(self.sup))
    def AllChamps(self):
        print(self.allchamps)
    def randTop(self):
        return self.top[random.randint(0,len(self.top)-1)]
    def randJg(self):
        return self.jg[random.randint(0,len(self.jg)-1)]
    def randMid(self):
        return self.mid[random.randint(0,len(self.mid)-1)]
    def randBot(self):
        return self.bot[random.randint(0,len(self.bot)-1)]
    def randSup(self):
        return self.sup[random.randint(0,len(self.sup)-1)]
    def allRand(self):
        return self.allchamps[random.randint(0,len(self.allchamps)-1)]
    def smartRandTeam(self):
        return (Champions.randTop(self), Champions.randJg(self), Champions.randMid(self), Champions.randBot(self), Champions.randSup(self))
    def dumbRandTeam(self):
        return (self.allchamps[0], self.allchamps[1], self.allchamps[2], self.allchamps[3], self.allchamps[4]) 
class Runes:
    def __init__(self):
        self.precision = [["Press the Attack", "Lethal Tempo", "Fleet Footwork", "Conqueror"], ["Overheal", "Triumph", "Presence of Mind"],
                          ["Legend: Alacrity", "Legend: Tenacity", "Legend: Bloodline"], ["Coup de Grace", "Cut Down", "Last Stand"]]
        self.domination = [["Electrocute", "Predator", "Dark Harvest", "Hail of Blades"], ["Cheap Shot", "Taste of Blood", "Sudden Impact"],
                           ["Zombie Ward", "Ghost Poro", "Eyeball Colection"], ["Ravenous Hunter", "Ingenious Hunter", "Relentless Hunter", "Ultimate Hunter"]]
        self.sorcery = [["Summon Aery", "Arcane Comet", "Phase Rush"], ["Nullifying Orb", "Manaflow Band", "Nimbus Cloak"],
                        ["Trancendence", "Celerity", "Absolute Focus"], ["Scorch", "Waterwalking", "Gathering Storm"]]
        self.resolve = [["Grasp of the Undying", "Aftershock", "Guardian"], ["Demolish", "Font of Life", "Shield Bash"],
                        ["Conditioning", "Second Wind", "Bone Plating"], ["Overgrowth", "Revitalize", "Unflinching"]]
        self.inspiration = [["Glacial Augment", "Unsealed Spellbook", "First Strike"], ["Hextech Flashtraption", "Magical Footwear", "Perfect Timing"],
                            ["Future's Market", "Minion Dematerializer", "Biscuit Delivery"], ["Cosmic Insight", "Approach Velocity", "Time Warp Tonic"]]
        self.shards = [["Adaptive Force", "Attack Speed", "Ability Haste"], ["Adaptive Force", "Armor", "Magic Resistance"], ["Bonus Health", "Armor", "Magic Resistance"]]
        self.runepaths = ["Precision", "Domination", "Sorcery", "Resolve", "Inspiration"]
    def makeRunepage(self):
        self.primary = self.runepaths[random.randint(0,len(self.runepaths)-1)]
        self.secondary = self.runepaths[random.randint(0,len(self.runepaths)-1)]
        while self.secondary == self.primary:
            self.secondary = self.runepaths[random.randint(0,len(self.runepaths)-1)]
        self.runesdict = {"Precision": self.precision, "Domination": self.domination, "Sorcery": self.sorcery, "Resolve": self.resolve, "Inspiration": self.inspiration}
        self.rune_primary = self.runesdict[self.primary]
        self.rune_secondary = self.runesdict[self.secondary]
        self.rune_secondary = self.rune_secondary[1:]
        self.keystone = self.rune_primary[0][random.randint(0,len(self.rune_primary[0])-1)]
        self.primary1 = self.rune_primary[1][random.randint(0,len(self.rune_primary[1])-1)]
        self.primary2 = self.rune_primary[2][random.randint(0,len(self.rune_primary[2])-1)]
        self.primary3 = self.rune_primary[3][random.randint(0,len(self.rune_primary[3])-1)]
        self.secondary_index1 = random.randint(0,2)
        self.secondary_index2 = random.randint(0,2)
        while self.secondary_index2 == self.secondary_index1:
            self.secondary_index2 = random.randint(0,2)
        self.secondary_index_list = [self.secondary_index1,self.secondary_index2]
        self.secondary_index_list.sort()
        self.secondary1 = self.rune_secondary[self.secondary_index_list[0]][random.randint(0,len(self.rune_secondary[self.secondary_index_list[0]])-1)]
        self.secondary2 = self.rune_secondary[self.secondary_index_list[1]][random.randint(0,len(self.rune_secondary[self.secondary_index_list[1]])-1)]
        self.shard1 = self.shards[0][random.randint(0,len(self.shards[0])-1)]
        self.shard2 = self.shards[1][random.randint(0,len(self.shards[1])-1)]
        self.shard3 = self.shards[2][random.randint(0,len(self.shards[2])-1)]
        return self.keystone, self.primary1, self.primary2, self.primary3, self.secondary1, self.secondary2, self.shard1, self.shard2, self.shard3
class Champ_Runes(Champions, Runes):
    def __init__(self):
        Champions.__init__(self)
        Runes.__init__(self)
        self.runes = Runes
        self.runes = self.runes.makeRunepage(self)
        i = 1
        while i != 0:
            print('Would you like a random rune page? (Type: "runes") \nWould you like a random champion from a specific lane? (Type: "top", "jg", "mid", "bot", or "sup") \nDo you want a random champion from all roles? (Type: "random") \nDo you want a random team with champions in their appropriate roles? (Type: "randomteam1") \nDo you would like a completely random team? (Type: "randomteam2")')
            userinput = input("Type Choice Here: ")
            if userinput == "top":
                self.randomchamp = Champions
                self.randomchamp = self.randomchamp.randTop(self)
                i = 0
                j = 0
            elif userinput == "jg":
                self.randomchamp = Champions
                self.randomchamp = self.randomchamp.randJg(self)
                i = 0
                j = 0
            elif userinput == "mid":
                self.randomchamp = Champions
                self.randomchamp = self.randomchamp.randMid(self)
                i = 0
                j = 0
            elif userinput == "bot":
                self.randomchamp = Champions
                self.randomchamp = self.randomchamp.randBot(self)
                i = 0
                j = 0
            elif userinput == "sup":
                self.randomchamp = Champions
                self.randomchamp = self.randomchamp.randSup(self)
                i = 0
                j = 0
            elif userinput == "random":
                self.randomchamp = Champions
                self.randomchamp = self.randomchamp.allRand(self)
                i = 0
                j = 0
            elif userinput == "runes":
                i = 0
                j = 1
            elif userinput == "randomteam1":
                self.randomchamptuple = Champions
                self.randomchamptuple = self.randomchamptuple.smartRandTeam(self)
                i = 0
                j = 2
            elif userinput == "randomteam2":
                self.randomchamptuple = Champions
                self.randomchamptuple = self.randomchamptuple.dumbRandTeam(self)
                i = 0
                j = 2
            else:
                print("ERROR: Please type one of the options below:")
        if j == 0:
            k = 1
            while k != 0:
                userinput2 = input('Would you like to create a random rune page for your champion ({})? \nPlease type "yes" or "no" here: '.format(self.randomchamp))
                if userinput2 == "yes":
                    print()
                    print("Champion: {}".format(self.randomchamp))
                    print()
                    print("Primary Page: {}".format(self.primary))
                    print("Keystone: {}".format(self.keystone))
                    print("Minor Rune One: {}".format(self.primary1))
                    print("Minor Rune Two: {}".format(self.primary2))
                    print("Minor Rune Three: {}".format(self.primary3))
                    print()
                    print("Secondary Page: {}".format(self.secondary))
                    print("Minor Rune One: {}".format(self.secondary1))
                    print("Minor Rune Two: {}".format(self.secondary2))
                    print()
                    print("Shard One: {}".format(self.shard1))
                    print("Shard Two: {}".format(self.shard2))
                    print("Shard Three: {}".format(self.shard3))
                    k = 0
                elif userinput2 == "no":
                    print()
                    print("Champion: {}".format(self.randomchamp))
                    k = 0
                else:
                    print('ERROR: Please type "yes" or "no"')
        elif j == 1:
            print()
            print("Primary Page: {}".format(self.primary))
            print("Keystone: {}".format(self.keystone))
            print("Minor Rune One: {}".format(self.primary1))
            print("Minor Rune Two: {}".format(self.primary2))
            print("Minor Rune Three: {}".format(self.primary3))
            print()
            print("Secondary Page: {}".format(self.secondary))
            print("Minor Rune One: {}".format(self.secondary1))
            print("Minor Rune Two: {}".format(self.secondary2))
            print()
            print("Shard One: {}".format(self.shard1))
            print("Shard Two: {}".format(self.shard2))
            print("Shard Three: {}".format(self.shard3))
        else:
            print("Random Team:")
            print("Top: {}".format(self.randomchamptuple[0]))
            print("Jungle: {}".format(self.randomchamptuple[1]))
            print("Mid: {}".format(self.randomchamptuple[2]))
            print("Bot: {}".format(self.randomchamptuple[3]))
            print("Support: {}".format(self.randomchamptuple[4]))
if __name__ == "__main__":
    Champ_Runes()