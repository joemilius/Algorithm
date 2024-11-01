vowels = "aeiou"

while(True):
    userinput = input("Please enter a word or phrase (type exit to end): ")
    if userinput.lower() == "exit":
        break
    else:
        consonantcount = 0
        vowelcount = 0
        for char in userinput:
            if char.lower() not in vowels:
                consonantcount += 1
            else:
                vowelcount += 1
        print ("Consonants: ",consonantcount," and vowels: ",vowelcount)