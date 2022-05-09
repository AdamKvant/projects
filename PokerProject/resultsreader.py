def reader():
    with open("PokerProject/winning_hand.csv") as file:
        contents = file.read()
        lst = contents.split("\n")
        lst = lst[1::]
        RF = lst.count("Royal Flush")
        SF = lst.count("Straight Flush")
        Four = lst.count("Four of a Kind")
        FH = lst.count("Full House")
        F = lst.count("Flush")
        S = lst.count("Straight")
        Three = lst.count("Three of a Kind")
        TP = lst.count("Two Pair")
        P = lst.count("Pair")
        HC = lst.count("High Card")
        RFpercent = (RF/len(lst)) * 100
        SFpercent = (SF/len(lst)) * 100
        Fourpercent = (Four/len(lst)) * 100
        FHpercent = (FH/len(lst)) * 100
        Fpercent = (F/len(lst)) * 100
        Spercent = (S/len(lst)) * 100
        Threepercent = (Three/len(lst)) * 100
        TPpercent = (TP/len(lst)) * 100
        Ppercent = (P/len(lst)) * 100
        HCpercent = (HC/len(lst)) * 100
        print("Percent of Royal Flush ",RFpercent,"%", " in a sample size: ", len(lst),sep="")
        print("Percent of Straight Flush ",SFpercent,"%", " in a sample size: ", len(lst),sep="")
        print("Percent of Four of a Kind ",Fourpercent,"%", " in a sample size: ", len(lst),sep="")
        print("Percent of Full House ",FHpercent,"%", " in a sample size: ", len(lst),sep="")
        print("Percent of Flush ",Fpercent,"%", " in a sample size: ", len(lst),sep="")
        print("Percent of Straight ",Spercent,"%", " in a sample size: ", len(lst),sep="")
        print("Percent of Three of a Kind ",Threepercent,"%", " in a sample size: ", len(lst),sep="")
        print("Percent of Two Pair ",TPpercent,"%", " in a sample size: ", len(lst),sep="")
        print("Percent of Pair ",Ppercent,"%", " in a sample size: ", len(lst),sep="")
        print("Percent of High Card ",HCpercent,"%", " in a sample size: ", len(lst),sep="")
reader()