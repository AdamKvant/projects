# Adam Kvant
import random
class Wordle:
    def __init__(self):
        with open("Wordle\words.txt", "r") as file:
                self.words = file.read()
                self.words = self.words.split("\n")
                self.five_letter_list = []
                for word in self.words:
                    if len(word) == 5:
                        self.five_letter_list.append(word)
                random.shuffle(self.five_letter_list)
                self.random_word_location = random.randint(0,len(self.five_letter_list)-1)
                self.puzzle_word = self.five_letter_list[self.random_word_location]
                Wordle.Game(self,self.puzzle_word)
    def Game(self, word):
        print("Wordle Fun!")
        letter_dict = {"a": 1,"b": 2,"c": 3,"d": 4,"e": 5,"f": 6,"g": 7,"h": 8,"i": 9,"j": 10,"k": 11,"l": 12,"m": 13,
                       "n": 14,"o": 15,"p": 16,"q": 17,"r": 18,"s": 19,"t": 20,"u": 21,"v": 22,"w": 23,"x": 24,"y": 25,"z": 26,}
        number_dict = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k", 12: "l", 13: "m", 
                       14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20: "t", 21: "u", 22: "v", 23: "w", 24: "x", 25: "y", 26: "y", }
        self.attempts_list = ["_ _ _ _ _","_ _ _ _ _","_ _ _ _ _","_ _ _ _ _","_ _ _ _ _","_ _ _ _ _"]
        for item in range(len(self.attempts_list)):
            self.attempts_list[item] = self.attempts_list[item].split(" ")
        self.letters_in_word = []
        self.letters_used = []
        self.puzzle_word = word
        attempts = 0
        used_attempts = 0
        while attempts < 6:
            i = 0
            while i != 1:
                self.userinput = input("Please type your guess here: ")
                if len(self.userinput) == 5:
                    i = 1
                else:
                    print("ERROR: Please type a five letter word")
            self.userinput = self.userinput.lower()
            self.userinput_orig = self.userinput
            self.userinput = [char for char in self.userinput]
            for char in range(len(self.userinput)):
                if self.userinput[char] == self.puzzle_word[char]:
                    if char == 0:
                        self.attempts_list[attempts][0]= self.userinput[char]
                    elif char == 1:
                        self.attempts_list[attempts][1]= self.userinput[char]
                    elif char == 2:
                        self.attempts_list[attempts][2]= self.userinput[char]
                    elif char == 3:
                        self.attempts_list[attempts][3]= self.userinput[char]
                    elif char == 4:
                        self.attempts_list[attempts][4]= self.userinput[char]
                if self.userinput[char] in self.puzzle_word:
                    self.letters_in_word.append(self.userinput[char])
                else:
                    self.letters_used.append(self.userinput[char])
            for val in range(0,attempts+1):
                print(self.attempts_list[val])
            self.letters_in_word = set(self.letters_in_word)
            self.letters_in_word = list(self.letters_in_word)
            self.letters_used = set(self.letters_used)
            self.letters_used = list(self.letters_used)
            for letter in self.letters_used:
                letter = letter_dict
            for letter in range(len(self.letters_used)):
                self.letters_used[letter] = letter_dict[self.letters_used[letter]]
            self.letters_used.sort()
            for letter in range(len(self.letters_used)):
                self.letters_used[letter] = number_dict[self.letters_used[letter]]
            for letter in range(len(self.letters_in_word)):
                self.letters_in_word[letter] = letter_dict[self.letters_in_word[letter]]
            self.letters_in_word.sort()
            for letter in range(len(self.letters_in_word)):
                self.letters_in_word[letter] = number_dict[self.letters_in_word[letter]]
            print("Letters in the word:", self.letters_in_word)
            print("Used letters not in word:", self.letters_used)
            if self.userinput_orig == self.puzzle_word:
                attempts = 6
                self.outcome = True 
            if 6-attempts < 1 and self.outcome == True:
                print("You won in {} attempts!".format(used_attempts + 1))
                with open("Wordle\streak.txt", "r") as file:
                    self.streak = file.read()
                    self.streak = self.streak.split("\n")
                    self.streak.append("1")
                    self.streaklen = len(self.streak)
                    self.streak = "\n".join(self.streak)
                with open("Wordle\streak.txt", "w") as file:
                    file.write(self.streak)
                print("Your streak is: {}".format(self.streaklen-1))
                userplay = input('Would you like to play again? Type "yes", or "no": ')
                if userplay == "yes":
                    Wordle()
                else:
                    pass
            elif 6 - attempts > 1:
                print("You have {} attempts remaining".format(5-attempts))
            else:
                with open("Wordle\streak.txt", "r") as file:
                    self.streak = file.read()
                    self.streak = self.streak.split("\n")
                    self.streak.append("1")
                    self.streaklen = len(self.streak)
                    self.streak = "\n".join(self.streak)
                with open("Wordle\streak.txt", "w") as file:
                    pass
                print("You have lost and your streak has been reset")
                print("Your streak was: {}".format(self.streaklen-1))
                print("The word was: {}".format(self.puzzle_word))
                userplay = input('Would you like to play again? Type "yes", or "no": ')
                if userplay == "yes":
                    Wordle()
                else:
                    pass                
            used_attempts += 1
            attempts += 1
if __name__ == "__main__":
    Wordle()

        
            