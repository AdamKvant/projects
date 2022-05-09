import random
import time
def birthday(people=23):
    birthday_list = []
    for person in range(0,people):
        iterate = random.randint(0,366)
        birthday_list.append(iterate)
    print(birthday_list)
    duplicate_list = []        
    for value in range(0,366):
        bday_count = birthday_list.count(value)
        if bday_count >=2:
            duplicate_list.append(value)
    list.sort(duplicate_list)
    if len(duplicate_list) >= 1:
        print("There is a duplicate birthday on this day of the year:",duplicate_list)
        with open("birthday/birthday_data.csv") as file:
            contents = file.read()
            contents += "\n{}".format("1")
        with open("birthday/birthday_data.csv","w") as file:
            file.write(contents)
    else:
        print("There are no dublicate birthdays")
        with open("birthday/birthday_data.csv") as file:
            contents = file.read()
            contents += "\n{}".format("0")
        with open("birthday/birthday_data.csv","w") as file:
            file.write(contents)
if __name__ == "__main__":
    #i = 1
    #while i != 0:
        #people = int(input("Enter a number of people (Minimum 2): "))
        #if people >= 2:
            #i = 0
            #birthday(people)
    tic = time.perf_counter()
    i = 100000
    while i > 0:
        birthday()
        i -= 1
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