#Adam Kvant
import time
import random
import csv
class Poker:
    def __init__(self,players):
        self.playercount = players
        self.playerlst = []
        while len(self.playerlst) < self.playercount:
            self.playerlst.append([])
        Player(self.playerlst)
    def getPlayerCount(self):
        return self.playercount
class Deck(Poker):
    def __init__(self):
        self.deck = ["AD","AC","AH","AS","2D","2C","2H","2S","3D","3C","3H","3S"
            ,"4D","4C","4H","4S","5D","5C","5H","5S","6D","6C","6H","6S","7D","7C","7H"
            ,"7S","8D","8C","8H","8S","9D","9C","9H","9S","TD","TC","TH","TS","JD","JC"
            ,"JH","JS","QD","QC","QH","QS","KD","KC","KH","KS"]
        random.shuffle(self.deck)
class Player():
    def __init__(self,players):
        Deck.__init__(self)
        self.playerlst = players
        for player in range(len(self.playerlst)):
            self.playerlst[player].append(self.deck[0])
            self.deck = self.deck[1:]
        for player in range(len(self.playerlst)):
            self.playerlst[player].append(self.deck[0])
            self.deck = self.deck[1:]
        #print(self.playerlst)
        self.board = [self.deck[1],self.deck[2],self.deck[3],self.deck[5],self.deck[7]]
        #print(self.board)
        Gameplay.__init__(self,self.playerlst,self.board)
class Gameplay:
    def __init__(self,players,board):
        self.playerlst = players
        self.board = board
        self.playerrank = []
        self.playersuit = []
        self.playerhand = []
        self.playerdict = []
        while len(self.playerdict) < len(self.playerlst):
            self.playerdict.append({})
        for i in range(len(self.playerlst)):
            for value in range(len(self.board)):
                self.playerlst[i].append(self.board[value])
        while len(self.playerrank) < len(self.playerlst):
            self.playerrank.append([])
        while len(self.playersuit) < len(self.playerlst):
            self.playersuit.append([])
        while len(self.playerhand) < len(self.playerlst):
            self.playerhand.append([[],[],[],[],[],[],[],[],[],[]])
        for j in range(len(self.playerlst)):
            for k in range(len(self.playerlst[j])):
                self.playerrank[j].append(self.playerlst[j][k][0])
        for j in range(len(self.playerlst)):
            for k in range(len(self.playerlst[j])):
                self.playersuit[j].append(self.playerlst[j][k][1])
        for player in range(len(self.playerlst)):
            Gameplay.isThree(self,player)
            Gameplay.isTwoPair(self,player)
            Gameplay.isPair(self,player)
            Gameplay.isFlush(self,player)
            Gameplay.isStraight(self,player)
            Gameplay.isFour(self,player)
            Gameplay.isFullHouse(self,player)
            Gameplay.isRoyalFlush(self,player)
            Gameplay.isStraightFlush(self,player)
            Gameplay.isHigh(self,player)
            self.carddict = {2: "Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Jack",12:"Queen",13:"King",14:"Ace"}
        for player in range(len(self.playerhand)):
            if len(self.playerhand[player][0]) > 0:
                self.playerdict[player]["Royal Flush"] = "True"
            if len(self.playerhand[player][1]) > 0:
                self.playerdict[player]["Straight Flush"] = "SF"
            if len(self.playerhand[player][2]) > 0:
                fourkindlst = []
                for val in range(len(self.playerhand[player][2])):
                    fourkindlst.append(self.carddict[self.playerhand[player][2][val]])
                self.playerdict[player]["Four of a Kind"] = set(fourkindlst)
            if len(self.playerhand[player][3]) > 0:
                fullhouselst = []
                for val in range(len(self.playerhand[player][3])):
                    fullhouselst.append(self.carddict[self.playerhand[player][3][val]])
                self.playerdict[player]["Full House"] = set(fullhouselst)
            if len(self.playerhand[player][4]) > 0:
                flushlst = []
                for val in range(len(self.playerhand[player][4])):
                    flushlst.append(self.carddict[self.playerhand[player][4][val]])
                self.playerdict[player]["Flush"] = set(flushlst)
            if len(self.playerhand[player][5]) > 0:
                straightlst = []
                for val in range(len(self.playerhand[player][5])):
                    straightlst.append(self.carddict[self.playerhand[player][5][val]])
                self.playerdict[player]["Straight"] = set(straightlst)
            if len(self.playerhand[player][6]) > 0:
                threekindlst = []
                for val in range(len(self.playerhand[player][6])):
                    threekindlst.append(self.carddict[self.playerhand[player][6][val]])
                self.playerdict[player]["Three of a Kind"] = set(threekindlst)
            if len(self.playerhand[player][7]) > 0:
                twopairlst = []
                for val in range(len(self.playerhand[player][7])):
                    twopairlst.append(self.carddict[self.playerhand[player][7][val]])
                self.playerdict[player]["Two Pair"] = set(twopairlst)
            if len(self.playerhand[player][8]) > 0:
                pairlst = []
                for val in range(len(self.playerhand[player][8])):
                    pairlst.append(self.carddict[self.playerhand[player][8][val]])
                self.playerdict[player]["Pair"] = set(pairlst)
            if len(self.playerhand[player][9]) > 0:
                highcardlst = []
                for val in range(len(self.playerhand[player][9])):
                    highcardlst.append(self.carddict[self.playerhand[player][9][val]])
                self.playerdict[player]["High Card"] = set(highcardlst)
        for player in range(len(self.playerdict)):
            #print("Player{} has: {}".format(player + 1, self.playerdict[player]))
            pass
        Gameplay.Winner(self,self.playerdict)
    
    def isRoyalFlush(self,player):
        if self.playerlst[player].count("AH") > 0 and self.playerlst[player].count("KH") > 0 and self.playerlst[player].count("QH") > 0 and self.playerlst[player].count("JH") > 0 and self.playerlst[player].count("TH") > 0: 
            self.playerhand[player][0].append(14)
        elif self.playerlst[player].count("AC") > 0 and self.playerlst[player].count("KC") > 0 and self.playerlst[player].count("QC") > 0 and self.playerlst[player].count("JC") > 0 and self.playerlst[player].count("TC") > 0: 
            self.playerhand[player][0].append(14)
        elif self.playerlst[player].count("AS") > 0 and self.playerlst[player].count("KS") > 0 and self.playerlst[player].count("QS") > 0 and self.playerlst[player].count("JS") > 0 and self.playerlst[player].count("TS") > 0: 
            self.playerhand[player][0].append(14)
        elif self.playerlst[player].count("AD") > 0 and self.playerlst[player].count("KD") > 0 and self.playerlst[player].count("QD") > 0 and self.playerlst[player].count("JD") > 0 and self.playerlst[player].count("TD") > 0: 
            self.playerhand[player][0].append(14)
    def isStraightFlush(self,player):
        if self.playerlst[player].count("AH") > 0 and self.playerlst[player].count("KH") > 0 and self.playerlst[player].count("QH") > 0 and self.playerlst[player].count("JH") > 0 and self.playerlst[player].count("TH") > 0: 
            self.playerhand[player][1].append(14)
        elif self.playerlst[player].count("KH") > 0 and self.playerlst[player].count("QH") > 0 and self.playerlst[player].count("JH") > 0 and self.playerlst[player].count("TH") > 0 and self.playerlst[player].count("9H") > 0: 
            self.playerhand[player][1].append(13)
        elif self.playerlst[player].count("QH") > 0 and self.playerlst[player].count("JH") > 0 and self.playerlst[player].count("TH") > 0 and self.playerlst[player].count("9H") > 0 and self.playerlst[player].count("8H") > 0: 
            self.playerhand[player][1].append(12)
        elif self.playerlst[player].count("JH") > 0 and self.playerlst[player].count("TH") > 0 and self.playerlst[player].count("9H") > 0 and self.playerlst[player].count("8H") > 0 and self.playerlst[player].count("7H") > 0: 
            self.playerhand[player][1].append(11) 
        elif self.playerlst[player].count("TH") > 0 and self.playerlst[player].count("9H") > 0 and self.playerlst[player].count("8H") > 0 and self.playerlst[player].count("7H") > 0 and self.playerlst[player].count("6H") > 0: 
            self.playerhand[player][1].append(10)
        elif self.playerlst[player].count("9H") > 0 and self.playerlst[player].count("8H") > 0 and self.playerlst[player].count("7H") > 0 and self.playerlst[player].count("6H") > 0 and self.playerlst[player].count("5H") > 0: 
            self.playerhand[player][1].append(9)
        elif self.playerlst[player].count("8H") > 0 and self.playerlst[player].count("7H") > 0 and self.playerlst[player].count("6H") > 0 and self.playerlst[player].count("5H") > 0 and self.playerlst[player].count("4H") > 0: 
            self.playerhand[player][1].append(8)
        elif self.playerlst[player].count("7H") > 0 and self.playerlst[player].count("6H") > 0 and self.playerlst[player].count("5H") > 0 and self.playerlst[player].count("4H") > 0 and self.playerlst[player].count("3H") > 0: 
            self.playerhand[player][1].append(7)
        elif self.playerlst[player].count("6H") > 0 and self.playerlst[player].count("5H") > 0 and self.playerlst[player].count("4H") > 0 and self.playerlst[player].count("3H") > 0 and self.playerlst[player].count("2H") > 0: 
            self.playerhand[player][1].append(6)
        elif self.playerlst[player].count("5H") > 0 and self.playerlst[player].count("4H") > 0 and self.playerlst[player].count("3H") > 0 and self.playerlst[player].count("2H") > 0 and self.playerlst[player].count("AH") > 0: 
            self.playerhand[player][1].append(5)
        elif self.playerlst[player].count("AD") > 0 and self.playerlst[player].count("KD") > 0 and self.playerlst[player].count("QD") > 0 and self.playerlst[player].count("JD") > 0 and self.playerlst[player].count("TD") > 0: 
            self.playerhand[player][1].append(14)
        elif self.playerlst[player].count("KD") > 0 and self.playerlst[player].count("QD") > 0 and self.playerlst[player].count("JD") > 0 and self.playerlst[player].count("TD") > 0 and self.playerlst[player].count("9D") > 0: 
            self.playerhand[player][1].append(13)
        elif self.playerlst[player].count("QD") > 0 and self.playerlst[player].count("JD") > 0 and self.playerlst[player].count("TD") > 0 and self.playerlst[player].count("9D") > 0 and self.playerlst[player].count("8D") > 0: 
            self.playerhand[player][1].append(12)
        elif self.playerlst[player].count("JD") > 0 and self.playerlst[player].count("TD") > 0 and self.playerlst[player].count("9D") > 0 and self.playerlst[player].count("8D") > 0 and self.playerlst[player].count("7D") > 0: 
            self.playerhand[player][1].append(11) 
        elif self.playerlst[player].count("TD") > 0 and self.playerlst[player].count("9D") > 0 and self.playerlst[player].count("8D") > 0 and self.playerlst[player].count("7D") > 0 and self.playerlst[player].count("6D") > 0: 
            self.playerhand[player][1].append(10)
        elif self.playerlst[player].count("9D") > 0 and self.playerlst[player].count("8D") > 0 and self.playerlst[player].count("7D") > 0 and self.playerlst[player].count("6D") > 0 and self.playerlst[player].count("5D") > 0: 
            self.playerhand[player][1].append(9)
        elif self.playerlst[player].count("8D") > 0 and self.playerlst[player].count("7D") > 0 and self.playerlst[player].count("6D") > 0 and self.playerlst[player].count("5D") > 0 and self.playerlst[player].count("4D") > 0: 
            self.playerhand[player][1].append(8)
        elif self.playerlst[player].count("7D") > 0 and self.playerlst[player].count("6D") > 0 and self.playerlst[player].count("5D") > 0 and self.playerlst[player].count("4D") > 0 and self.playerlst[player].count("3D") > 0: 
            self.playerhand[player][1].append(7)
        elif self.playerlst[player].count("6D") > 0 and self.playerlst[player].count("5D") > 0 and self.playerlst[player].count("4D") > 0 and self.playerlst[player].count("3D") > 0 and self.playerlst[player].count("2D") > 0: 
            self.playerhand[player][1].append(6)
        elif self.playerlst[player].count("5D") > 0 and self.playerlst[player].count("4D") > 0 and self.playerlst[player].count("3D") > 0 and self.playerlst[player].count("2D") > 0 and self.playerlst[player].count("AD") > 0: 
            self.playerhand[player][1].append(5)
        elif self.playerlst[player].count("AC") > 0 and self.playerlst[player].count("KC") > 0 and self.playerlst[player].count("QC") > 0 and self.playerlst[player].count("JC") > 0 and self.playerlst[player].count("TC") > 0: 
            self.playerhand[player][1].append(14)
        elif self.playerlst[player].count("KC") > 0 and self.playerlst[player].count("QC") > 0 and self.playerlst[player].count("JC") > 0 and self.playerlst[player].count("TC") > 0 and self.playerlst[player].count("9C") > 0: 
            self.playerhand[player][1].append(13)
        elif self.playerlst[player].count("QC") > 0 and self.playerlst[player].count("JC") > 0 and self.playerlst[player].count("TC") > 0 and self.playerlst[player].count("9C") > 0 and self.playerlst[player].count("8C") > 0: 
            self.playerhand[player][1].append(12)
        elif self.playerlst[player].count("JC") > 0 and self.playerlst[player].count("TC") > 0 and self.playerlst[player].count("9C") > 0 and self.playerlst[player].count("8C") > 0 and self.playerlst[player].count("7C") > 0: 
            self.playerhand[player][1].append(11) 
        elif self.playerlst[player].count("TC") > 0 and self.playerlst[player].count("9C") > 0 and self.playerlst[player].count("8C") > 0 and self.playerlst[player].count("7C") > 0 and self.playerlst[player].count("6C") > 0: 
            self.playerhand[player][1].append(10)
        elif self.playerlst[player].count("9C") > 0 and self.playerlst[player].count("8C") > 0 and self.playerlst[player].count("7C") > 0 and self.playerlst[player].count("6C") > 0 and self.playerlst[player].count("5C") > 0: 
            self.playerhand[player][1].append(9)
        elif self.playerlst[player].count("8C") > 0 and self.playerlst[player].count("7C") > 0 and self.playerlst[player].count("6C") > 0 and self.playerlst[player].count("5C") > 0 and self.playerlst[player].count("4C") > 0: 
            self.playerhand[player][1].append(8)
        elif self.playerlst[player].count("7C") > 0 and self.playerlst[player].count("6C") > 0 and self.playerlst[player].count("5C") > 0 and self.playerlst[player].count("4C") > 0 and self.playerlst[player].count("3C") > 0: 
            self.playerhand[player][1].append(7)
        elif self.playerlst[player].count("6C") > 0 and self.playerlst[player].count("5C") > 0 and self.playerlst[player].count("4C") > 0 and self.playerlst[player].count("3C") > 0 and self.playerlst[player].count("2C") > 0: 
            self.playerhand[player][1].append(6)
        elif self.playerlst[player].count("5C") > 0 and self.playerlst[player].count("4C") > 0 and self.playerlst[player].count("3C") > 0 and self.playerlst[player].count("2C") > 0 and self.playerlst[player].count("AC") > 0: 
            self.playerhand[player][1].append(5)
        elif self.playerlst[player].count("AS") > 0 and self.playerlst[player].count("KS") > 0 and self.playerlst[player].count("QS") > 0 and self.playerlst[player].count("JS") > 0 and self.playerlst[player].count("TS") > 0: 
            self.playerhand[player][1].append(14)
        elif self.playerlst[player].count("KS") > 0 and self.playerlst[player].count("QS") > 0 and self.playerlst[player].count("JS") > 0 and self.playerlst[player].count("TS") > 0 and self.playerlst[player].count("9S") > 0: 
            self.playerhand[player][1].append(13)
        elif self.playerlst[player].count("QS") > 0 and self.playerlst[player].count("JS") > 0 and self.playerlst[player].count("TS") > 0 and self.playerlst[player].count("9S") > 0 and self.playerlst[player].count("8S") > 0: 
            self.playerhand[player][1].append(12)
        elif self.playerlst[player].count("JS") > 0 and self.playerlst[player].count("TS") > 0 and self.playerlst[player].count("9S") > 0 and self.playerlst[player].count("8S") > 0 and self.playerlst[player].count("7S") > 0: 
            self.playerhand[player][1].append(11) 
        elif self.playerlst[player].count("TS") > 0 and self.playerlst[player].count("9S") > 0 and self.playerlst[player].count("8S") > 0 and self.playerlst[player].count("7S") > 0 and self.playerlst[player].count("6S") > 0: 
            self.playerhand[player][1].append(10)
        elif self.playerlst[player].count("9S") > 0 and self.playerlst[player].count("8S") > 0 and self.playerlst[player].count("7S") > 0 and self.playerlst[player].count("6S") > 0 and self.playerlst[player].count("5S") > 0: 
            self.playerhand[player][1].append(9)
        elif self.playerlst[player].count("8S") > 0 and self.playerlst[player].count("7S") > 0 and self.playerlst[player].count("6S") > 0 and self.playerlst[player].count("5S") > 0 and self.playerlst[player].count("4S") > 0: 
            self.playerhand[player][1].append(8)
        elif self.playerlst[player].count("7S") > 0 and self.playerlst[player].count("6S") > 0 and self.playerlst[player].count("5S") > 0 and self.playerlst[player].count("4S") > 0 and self.playerlst[player].count("3S") > 0: 
            self.playerhand[player][1].append(7)
        elif self.playerlst[player].count("6S") > 0 and self.playerlst[player].count("5S") > 0 and self.playerlst[player].count("4S") > 0 and self.playerlst[player].count("3S") > 0 and self.playerlst[player].count("2S") > 0: 
            self.playerhand[player][1].append(6)
        elif self.playerlst[player].count("5S") > 0 and self.playerlst[player].count("4S") > 0 and self.playerlst[player].count("3S") > 0 and self.playerlst[player].count("2S") > 0 and self.playerlst[player].count("AS") > 0: 
            self.playerhand[player][1].append(5)        
    def isFour(self,player):
        if self.playerrank[player].count("A") > 3:
            self.playerhand[player][2].append(14)
        elif self.playerrank[player].count("K") > 3:
            self.playerhand[player][2].append(13)
        elif self.playerrank[player].count("Q") > 3:
            self.playerhand[player][2].append(12)
        elif self.playerrank[player].count("J") > 3:
            self.playerhand[player][2].append(11)
        elif self.playerrank[player].count("T") > 3:
            self.playerhand[player][2].append(10)
        elif self.playerrank[player].count("9") > 3:
            self.playerhand[player][2].append(9)
        elif self.playerrank[player].count("8") > 3:
            self.playerhand[player][2].append(8)
        elif self.playerrank[player].count("7") > 3:
            self.playerhand[player][2].append(7)
        elif self.playerrank[player].count("6") > 3:
            self.playerhand[player][2].append(6)
        elif self.playerrank[player].count("5") > 3:
            self.playerhand[player][2].append(5)
        elif self.playerrank[player].count("4") > 3:
            self.playerhand[player][2].append(4)
        elif self.playerrank[player].count("3") > 3:
            self.playerhand[player][2].append(3)
        elif self.playerrank[player].count("2") > 3:
            self.playerhand[player][2].append(2)
    def isFullHouse(self,player):
        if len(self.playerhand[player][8]) > 1 and len(self.playerhand[player][6]) > 0:
            for val in range(len(self.playerhand[player][6])):
                self.playerhand[player][3].append(self.playerhand[player][6][val])
            for val in range(len(self.playerhand[player][8])):
                if self.playerhand[player][8][val] != self.playerhand[player][6]:
                    self.playerhand[player][3].append(self.playerhand[player][8][val])
    def isFlush(self,player):
        if self.playersuit[player].count("D") > 4:
            if "AD" in self.playerlst[player]:
                self.playerhand[player][4].append(14)
            elif "KD" in self.playerlst[player]:
                self.playerhand[player][4].append(13)
            elif "QD" in self.playerlst[player]:
                self.playerhand[player][4].append(12)
            elif "JD" in self.playerlst[player]:
                self.playerhand[player][4].append(11)
            elif "TD" in self.playerlst[player]:
                self.playerhand[player][4].append(10)
            elif "9D" in self.playerlst[player]:
                self.playerhand[player][4].append(9)
            elif "8D" in self.playerlst[player]:
                self.playerhand[player][4].append(8)
            elif "7D" in self.playerlst[player]:
                self.playerhand[player][4].append(7)
            elif "6D" in self.playerlst[player]:
                self.playerhand[player][4].append(6)
            elif "5D" in self.playerlst[player]:
                self.playerhand[player][4].append(5)
            elif "4D" in self.playerlst[player]:
                self.playerhand[player][4].append(4)
            elif "3D" in self.playerlst[player]:
                self.playerhand[player][4].append(3)
            else:
                self.playerhand[player][9].append(2) 
        elif self.playersuit[player].count("C") > 4:
            if "AC" in self.playerlst[player]:
                self.playerhand[player][4].append(14)
            elif "KC" in self.playerlst[player]:
                self.playerhand[player][4].append(13)
            elif "QC" in self.playerlst[player]:
                self.playerhand[player][4].append(12)
            elif "JC" in self.playerlst[player]:
                self.playerhand[player][4].append(11)
            elif "TC" in self.playerlst[player]:
                self.playerhand[player][4].append(10)
            elif "9C" in self.playerlst[player]:
                self.playerhand[player][4].append(9)
            elif "8C" in self.playerlst[player]:
                self.playerhand[player][4].append(8)
            elif "7C" in self.playerlst[player]:
                self.playerhand[player][4].append(7)
            elif "6C" in self.playerlst[player]:
                self.playerhand[player][4].append(6)
            elif "5C" in self.playerlst[player]:
                self.playerhand[player][4].append(5)
            elif "4C" in self.playerlst[player]:
                self.playerhand[player][4].append(4)
            elif "3C" in self.playerlst[player]:
                self.playerhand[player][4].append(3)
            else:
                self.playerhand[player][4].append(2)
        elif self.playersuit[player].count("H") > 4:
            if "AH" in self.playerlst[player]:
                self.playerhand[player][4].append(14)
            elif "KH" in self.playerlst[player]:
                self.playerhand[player][4].append(13)
            elif "QH" in self.playerlst[player]:
                self.playerhand[player][4].append(12)
            elif "JH" in self.playerlst[player]:
                self.playerhand[player][4].append(11)
            elif "TH" in self.playerlst[player]:
                self.playerhand[player][4].append(10)
            elif "9H" in self.playerlst[player]:
                self.playerhand[player][4].append(9)
            elif "8H" in self.playerlst[player]:
                self.playerhand[player][4].append(8)
            elif "7H" in self.playerlst[player]:
                self.playerhand[player][4].append(7)
            elif "6H" in self.playerlst[player]:
                self.playerhand[player][4].append(6)
            elif "5H" in self.playerlst[player]:
                self.playerhand[player][4].append(5)
            elif "4H" in self.playerlst[player]:
                self.playerhand[player][4].append(4)
            elif "3H" in self.playerlst[player]:
                self.playerhand[player][4].append(3)
            else:
                self.playerhand[player][4].append(2)
        elif self.playersuit[player].count("S") > 4:
            if "AS" in self.playerlst[player]:
                self.playerhand[player][4].append(14)
            elif "KS" in self.playerlst[player]:
                self.playerhand[player][4].append(13)
            elif "QS" in self.playerlst[player]:
                self.playerhand[player][4].append(12)
            elif "JS" in self.playerlst[player]:
                self.playerhand[player][4].append(11)
            elif "TS" in self.playerlst[player]:
                self.playerhand[player][4].append(10)
            elif "9S" in self.playerlst[player]:
                self.playerhand[player][4].append(9)
            elif "8S" in self.playerlst[player]:
                self.playerhand[player][4].append(8)
            elif "7S" in self.playerlst[player]:
                self.playerhand[player][4].append(7)
            elif "6S" in self.playerlst[player]:
                self.playerhand[player][4].append(6)
            elif "5S" in self.playerlst[player]:
                self.playerhand[player][4].append(5)
            elif "4S" in self.playerlst[player]:
                self.playerhand[player][4].append(4)
            elif "3S" in self.playerlst[player]:
                self.playerhand[player][4].append(3)
            else:
                self.playerhand[player][4].append(2)
    def isStraight(self,player):
        aces = self.playerrank[player].count("A")
        twos = self.playerrank[player].count("2")
        threes = self.playerrank[player].count("3")
        fours = self.playerrank[player].count("4")
        fives = self.playerrank[player].count("5")
        sixes = self.playerrank[player].count("6")
        sevens = self.playerrank[player].count("7")
        eights = self.playerrank[player].count("8")
        nines = self.playerrank[player].count("9")
        tens = self.playerrank[player].count("T")
        jacks = self.playerrank[player].count("J")
        queens = self.playerrank[player].count("Q")
        kings = self.playerrank[player].count("K")
        if aces > 0 and kings > 0 and queens > 0 and jacks > 0 and tens > 0:
            self.playerhand[player][5].append(14)
        elif kings > 0 and queens > 0 and jacks > 0 and tens > 0 and nines > 0:
            self.playerhand[player][5].append(13)
        elif queens > 0 and jacks > 0 and tens > 0 and nines > 0 and eights > 0:
            self.playerhand[player][5].append(12)
        elif jacks > 0 and tens > 0 and nines > 0 and eights > 0 and sevens > 0:
            self.playerhand[player][5].append(11)
        elif tens > 0 and nines > 0 and eights > 0 and sevens > 0 and sixes > 0:
            self.playerhand[player][5].append(10)
        elif nines > 0 and eights > 0 and sevens > 0 and sixes > 0 and fives > 0:
            self.playerhand[player][5].append(9)
        elif eights > 0 and sevens > 0 and sixes > 0 and fives > 0 and fours > 0:
            self.playerhand[player][5].append(8)
        elif sevens > 0 and sixes > 0 and fives > 0 and fours > 0 and threes > 0:
            self.playerhand[player][5].append(7)
        elif sixes > 0 and fives > 0 and fours > 0 and threes > 0 and twos > 0:
            self.playerhand[player][5].append(6)
        elif fives > 0 and fours > 0 and threes > 0 and twos > 0 and aces > 0:
            self.playerhand[player][5].append(5)                
    def isThree(self,player):
        if self.playerrank[player].count("A") > 2:
            self.playerhand[player][6].append(14)
        elif self.playerrank[player].count("K") > 2:
            self.playerhand[player][6].append(13)
        elif self.playerrank[player].count("Q") > 2:
            self.playerhand[player][6].append(12)
        elif self.playerrank[player].count("J") > 2:
            self.playerhand[player][6].append(11)
        elif self.playerrank[player].count("T") > 2:
            self.playerhand[player][6].append(10)
        elif self.playerrank[player].count("9") > 2:
            self.playerhand[player][6].append(9)
        elif self.playerrank[player].count("8") > 2:
            self.playerhand[player][6].append(8)
        elif self.playerrank[player].count("7") > 2:
            self.playerhand[player][6].append(7)
        elif self.playerrank[player].count("6") > 2:
            self.playerhand[player][6].append(6)
        elif self.playerrank[player].count("5") > 2:
            self.playerhand[player][6].append(5)
        elif self.playerrank[player].count("4") > 2:
            self.playerhand[player][6].append(4)
        elif self.playerrank[player].count("3") > 2:
            self.playerhand[player][6].append(3)
        elif self.playerrank[player].count("2") > 2:
            self.playerhand[player][6].append(2)
    def isTwoPair(self,player):
        if self.playerrank[player].count("A") > 1:
            self.playerhand[player][7].append(14)
        if self.playerrank[player].count("K") > 1:
            self.playerhand[player][7].append(13)
        if self.playerrank[player].count("Q") > 1:
            self.playerhand[player][7].append(12)
        if self.playerrank[player].count("J") > 1:
            self.playerhand[player][7].append(11)
        if self.playerrank[player].count("T") > 1:
            self.playerhand[player][7].append(10)
        if self.playerrank[player].count("9") > 1:
            self.playerhand[player][7].append(9)
        if self.playerrank[player].count("8") > 1:
            self.playerhand[player][7].append(8)
        if self.playerrank[player].count("7") > 1:
            self.playerhand[player][7].append(7)
        if self.playerrank[player].count("6") > 1:
            self.playerhand[player][7].append(6)
        if self.playerrank[player].count("5") > 1:
            self.playerhand[player][7].append(5)
        if self.playerrank[player].count("4") > 1:
            self.playerhand[player][7].append(4)
        if self.playerrank[player].count("3") > 1:
            self.playerhand[player][7].append(3)
        if self.playerrank[player].count("2") > 1:
            self.playerhand[player][7].append(2)
        if len(self.playerhand[player][7]) > 1:
            pass
        else:
            self.playerhand[player][7] = []
    def isPair(self,player):
        if self.playerrank[player].count("A") > 1:
            self.playerhand[player][8].append(14)
        if self.playerrank[player].count("K") > 1:
            self.playerhand[player][8].append(13)
        if self.playerrank[player].count("Q") > 1:
            self.playerhand[player][8].append(12)
        if self.playerrank[player].count("J") > 1:
            self.playerhand[player][8].append(11)
        if self.playerrank[player].count("T") > 1:
            self.playerhand[player][8].append(10)
        if self.playerrank[player].count("9") > 1:
            self.playerhand[player][8].append(9)
        if self.playerrank[player].count("8") > 1:
            self.playerhand[player][8].append(8)
        if self.playerrank[player].count("7") > 1:
            self.playerhand[player][8].append(7)
        if self.playerrank[player].count("6") > 1:
            self.playerhand[player][8].append(6)
        if self.playerrank[player].count("5") > 1:
            self.playerhand[player][8].append(5)
        if self.playerrank[player].count("4") > 1:
            self.playerhand[player][8].append(4)
        if self.playerrank[player].count("3") > 1:
            self.playerhand[player][8].append(3)
        if self.playerrank[player].count("2") > 1:
            self.playerhand[player][8].append(2)
    def isHigh(self,player):
        if "A" in self.playerrank[player] and "A" not in self.playerhand[player][8] and "A" not in self.playerhand[player][7]:
            self.playerhand[player][9].append(14)
        elif "K" in self.playerrank[player] and "K" not in self.playerhand[player][8] and "K" not in self.playerhand[player][7]:
            self.playerhand[player][9].append(13)
        elif "Q" in self.playerrank[player] and "Q" not in self.playerhand[player][8] and "Q" not in self.playerhand[player][7]:
            self.playerhand[player][9].append(12)
        elif "J" in self.playerrank[player] and "J" not in self.playerhand[player][8] and "J" not in self.playerhand[player][7]:
            self.playerhand[player][9].append(11)
        elif "T" in self.playerrank[player] and "T" not in self.playerhand[player][8] and "T" not in self.playerhand[player][7]:
            self.playerhand[player][9].append(10)
        elif "9" in self.playerrank[player] and "9" not in self.playerhand[player][8] and "9" not in self.playerhand[player][7]:
            self.playerhand[player][9].append(9)
        elif "8" in self.playerrank[player] and "8" not in self.playerhand[player][8] and "8" not in self.playerhand[player][7]:
            self.playerhand[player][9].append(8)
        elif "7" in self.playerrank[player] and "7" not in self.playerhand[player][8] and "7" not in self.playerhand[player][7]:
            self.playerhand[player][9].append(7)
        elif "6" in self.playerrank[player] and "6" not in self.playerhand[player][8] and "6" not in self.playerhand[player][7]:
            self.playerhand[player][9].append(6)
        elif "5" in self.playerrank[player] and "5" not in self.playerhand[player][8] and "5" not in self.playerhand[player][7]:
            self.playerhand[player][9].append(5)
        elif "4" in self.playerrank[player] and "4" not in self.playerhand[player][8] and "4" not in self.playerhand[player][7]:
            self.playerhand[player][9].append(4)
        elif "3" in self.playerrank[player] and "3" not in self.playerhand[player][8] and "3" not in self.playerhand[player][7]:
            self.playerhand[player][9].append(3)
        else:
            self.playerhand[player][9].append(2)
    def Winner(self, playerdict):
        playerdict = self.playerdict
        player_win_con = []
        for player in range(len(playerdict)):
            player_win_con.append([0])
        for player in range(len(playerdict)):
            for key in playerdict[player]:
                if player_win_con[player] == [0]:
                    if key == "Royal Flush":
                        player_win_con[player] = [10]
                    elif key == "Straight Flush":
                        player_win_con[player] = [9]
                    elif key == "Four of a Kind":
                        player_win_con[player] = [8]
                    elif key == "Full House":
                        player_win_con[player] = [7]
                    elif key == "Flush":
                        player_win_con[player] = [6]
                    elif key == "Straight":
                        player_win_con[player] = [5]
                    elif key == "Three of a Kind":
                        player_win_con[player] = [4]
                    elif key == "Two Pair":
                        player_win_con[player] = [3]
                    elif key == "Pair":
                        player_win_con[player] = [2]
                    elif key == "High Card":
                        player_win_con[player] = [1]
        winning_hand = 0
        winning_index_list = []
        for player in range(len(player_win_con)):
            player_win_con[player].append(player)
        player_win_con.sort()
        player_win_con.reverse()
        for player in range(len(player_win_con)):
            current_val = player_win_con[player][0]
            if current_val >= winning_hand:
                winning_index_list.append(player_win_con[player][1])
                winning_hand = current_val
        winning_index_list.sort()
        winning_dict = {10: "Royal Flush", 9: "Straight Flush", 8: "Four of a Kind", 7: "Full House",
                        6: "Flush", 5: "Straight", 4: "Three of a Kind", 3: "Two Pair", 2: "Pair", 1: "High Card"}
        if len(winning_index_list) == 1:
                print("Player{} won with a {}!".format(winning_index_list[0]+1,winning_dict[winning_hand]))

        else:
            for index in winning_index_list:
                print("Player{} tied with a {}!".format(index + 1,winning_dict[winning_hand]))

        with open("PokerProject/winning_hand.csv") as file:
            contents = file.read()
            contents += "\n{}".format(winning_dict[winning_hand])
        with open("PokerProject/winning_hand.csv","w") as file:
            file.write(contents)
tic = time.perf_counter()
i = 0      
while i < 25000:
    Poker(7)
    i += 1
    print(i) 
toc = time.perf_counter()
total_time = toc - tic
days = total_time // 86400
rem_days = total_time % 86400
hours = rem_days // 3600
rem_hours = rem_days % 3600
minutes = rem_hours // 60
rem_minutes = rem_hours % 60
seconds = rem_minutes
print(f"Runtime: {days} days, {hours} hours, {minutes} minutes, {seconds: 0.4f} seconds")