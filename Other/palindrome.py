def palindrome(string):
    string = str(string)
    oldstr = string
    origninal_string_length = len(string)
    count = 0
    removelst = [" ",",",".","!","?","'","/"]
    for char in string:
        if char in removelst:
            count += 1
    if count != origninal_string_length:
        for char in removelst:
            string = string.replace(char,"")
    string = string.lower()
    string = [char for char in string]
    strlen = len(string)-1
    string = "".join(string)
    palindrome_count = 0
    for char in range(len(string)):
        if string[char] == string[strlen]:
            if strlen != 0:
                strlen -= 1
                palindrome_count += 1
        else:
            strlen -= 1
    if palindrome_count == len(string)-1:
        print('"',oldstr,'"'," is a Palindrome",sep="")
    else:
        print('"',oldstr,'"'," is not a Palindrome",sep="")



palindrome("Adam")
palindrome("racecar")
palindrome("Was it a car or a cat I saw")
palindrome("hancxxnah")
palindrome("  ")
palindrome("red rum, sir, is murder")
palindrome("?!!!")
palindrome(897)
palindrome("Don't nod.")
palindrome("Eva, can I see bees in a cave?")
palindrome("12/11/21")
palindrome("sator arepo tenet opera rotas.")
palindrome("?1d!")
palindrome("!aa!")
