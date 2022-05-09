
def reader():
    with open("birthday/birthday_data.csv") as file:
        contents = file.read()
        lst = contents.split("\n")
        lst = lst[1::]
        match = lst.count("1")
        nomatch = lst.count("0")
        matchpercent = (match/len(lst)) * 100
        nomatchpercent = (nomatch/len(lst)) * 100
        print("Percent of matching birthdays ",matchpercent,"%", " of a sample size: ", len(lst),sep="")
        print("Percent of nonmatching birthdays ",nomatchpercent,"%", " of a sample size: ", len(lst),sep="")
reader()