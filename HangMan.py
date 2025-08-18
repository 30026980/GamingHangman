import os
import time
import random
import Setup
import CheckingMethod
import UpdateSettings


def funStillInGame(intMissCheck, bolWordComplete):
    if intMissCheck >= 0 and bolWordComplete == False:
        return False
    else:
        return True
#Varibles Used for Guessing
intMissCheck = 7
strWord = ""
strQuessingWord = ""
bolWordComplete = False
strLetterQuesses = []

for i in range(30):
    print("\n")
    
#Setting up the Word
strWord = Setup.funGetRandomGame().lower()
strQuessingWord = Setup.funUnderScoreLine(strWord).lower()

#So we can stay in the game as long as you haven't lost/won
while funStillInGame(intMissCheck, bolWordComplete) == False:
    print(strQuessingWord)
    bolCheckVal = False
    
    #Looping for vailding the users input so we don't get something that can break it
    while bolCheckVal == False:
        strUserLetter = input().lower()
        #Checking if it isn't a symble
        if strUserLetter.isalnum() == True:
            
            #Checking if the Number/Letters has already been Played
            if CheckingMethod.funCheckQuesses(strUserLetter, strLetterQuesses) == True:
                
                #Checking to see if it is ONLY 1 Letter/Number
                if CheckingMethod.funCheckForOneLetter(strUserLetter) == True:
                    bolCheckVal = True
                    strLetterQuesses.append(strUserLetter)
                else:
                    print ("More then 1 Letter/Number Played")
            else:
                print("Already has been played")
        else:
            bolCheckVal = False
            print("Can only play Letters or Numbers")
    if funStillInGame(intMissCheck, bolWordComplete) == False:
        strTempQuessedWord = strQuessingWord
        
        strQuessingWord = CheckingMethod.funCheckLetters(strUserLetter, strWord, strQuessingWord)
        for i in range(30):
            print("\n")
        
        if strQuessingWord == strTempQuessedWord:
            intMissCheck -= 1
            print("Letter was not apart of the word - ", intMissCheck, " - wrong quesses left")
        else:
            print("letter was apart of the word -",)
            if strWord == strQuessingWord:
                bolWordComplete = True
        
if intMissCheck < 0:
    for i in range(30):
        print("\n")
    print("you lose")
else:
    for i in range(30):
        print("\n")
    print("you win")
print("The Word Was -", strWord)

a = input()