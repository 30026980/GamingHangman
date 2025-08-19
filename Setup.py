import os
import time
import random
import json

#Well this exists good luck reading it
#For Deciding if the guess word is going to be a Character Or a Game (May add more in the furture but idk)
def funCharacterOrGame():
    file_name = os.path.dirname(__file__)
    bolLoop = False
    
    #Opening the Json File for setting/ Run the function in UpdateSettings.py called funUpdatingSettings() if you are adding any new Lists and make them true
    with open (os.path.dirname(__file__) + '/Setting.json', 'r') as file:
        config = json.load(file)
        
    #For Vaildation
    while bolLoop == False:
        strUserWantsToQuess = input("Do you want to quess a Character (-C-) or a Game (-G-)")
        if strUserWantsToQuess.lower() == "g":
            #Grabing the settings for all of the games lists for what is set to true
            settings = config.get("Game", {})
            
            #i'm be honest i don't know how the hell this work but it does so idk
            lstEnabledGame = [key for key, value in settings.items() if value is True]
            for i in range(30):
                print("\n")
            print(lstEnabledGame)
            
            #Grabing the file and sending it
            file_name += "/WordLists/Games/" + random.choice(lstEnabledGame) + ".txt"
            bolLoop = True
        
        elif strUserWantsToQuess.lower() == "c":
            #Grabing the settings for all of the Characters lists for what is set to true
            settings = config.get("Character", {})
            
            #Again it works IDK how the hell it works
            lstEnabledCharacter = [key for key, value in settings.items() if value is True]
            for i in range(30):
                print("\n")
            print(lstEnabledCharacter)
            
            #Grabing the file and sending it
            file_name += "/WordLists/Characters/" + random.choice(lstEnabledCharacter) + ".txt"
            bolLoop = True
        else:
            for i in range(30):
                print("\n")
            print("Please Enter a character C or G")
    return file_name

#Choosing a random game from the list
def funGetRandomGame():
    #Because it hates me this is here
    file_name = ""
    
    #Seeing if the user wants to guess a game or a character
    file_name = funCharacterOrGame()
    strSelectedLine = None
    
    #Opening the file and grabing a random Word from the txt
    with open(file_name,) as GameFile:
        for i, line in enumerate(GameFile, start = 1):
            if random.randint(1,i) == 1:
                strSelectedLine = line.strip()
    return strSelectedLine
    
#Underscores the quessing word so the user can quess the word
def funUnderScoreLine(strWord = ""):
    count = 0
    strUnderScoreWord = ""
    for char in strWord:
        if strWord[count].isspace() != True:
            if strWord[count].isalnum() == True:
                strUnderScoreWord += "_"
            else:
                strUnderScoreWord += strWord[count]
        else:
            strUnderScoreWord += " "
        count += 1
    return strUnderScoreWord