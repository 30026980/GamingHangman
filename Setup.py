import os
import time
import random
import json


#Grabing the place of where the Wordlist will be
file_name = os.path.dirname(__file__) + '/WordLists/'

with open (os.path.dirname(__file__) + '/Setting.json', 'r') as file:
    config = json.load(file)

bolLoop = False
while bolLoop == False:
    strUserWantsToQuess = input("Do you want to quess a Character (-C-) or a Game (-G-)")
    if strUserWantsToQuess.lower == "g":
        settings = config.get("Game", {})
        lstEnabledGame = [key for key, value in settings.items() if value is True]
        file_name += random.choice(lstEnabledGame) + ".txt"
    elif strUserWantsToQuess.lower == "c":
        settings = config.get("Character", {})
        lstEnabledCharacter = [key for key, value in settings.items() if value is True]
        file_name += random.choice(lstEnabledCharacter) + ".txt"

def funGetRandomGame():
    strSelectedLine = None
    with open(file_name,) as GameFile:
        for i, line in enumerate(GameFile, start = 1):
            if random.randint(1,i) == 1:
                strSelectedLine = line.strip()
    return strSelectedLine
    
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
