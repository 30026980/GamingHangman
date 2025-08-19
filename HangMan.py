import os
import time
import random
import Setup
import CheckingMethod
import UpdateSettings


def funStillInGame(intMissCheck, bolWordComplete):
    if intMissCheck >= 1 and bolWordComplete == False:
        return False
    else:
        return True
#Varibles Used for Guessing
intMissCheck = 8
strWord = ""
strQuessingWord = ""
bolWordComplete = False
strLetterQuesses = []

#When This Apears it is to clean up the terminal so it looks nicer
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
        
        #For replacing the blank word with the letters needed, 1 = The Quessed Letter, 2 = the Full Word and 3 = the Current word
        strQuessingWord = CheckingMethod.funCheckLetters(strUserLetter, strWord, strQuessingWord)
        for i in range(30):
            print("\n")
        #if the quessed word is the same then say the letter is wrong
        if strQuessingWord == strTempQuessedWord:
            intMissCheck -= 1
            print("Letter was not apart of the word - ", intMissCheck, " - wrong quesses left")
        else:
            print("letter was apart of the word -",)
            if strWord == strQuessingWord:
                bolWordComplete = True
#if the quess count is 0 or lower then it shows you lose while if it is above you win        
if intMissCheck < 1:
    for i in range(30):
        print("\n")
    print("you lose")
else:
    for i in range(30):
        print("\n")
    print("you win")
print("The Word Was -", strWord)

#to pause the word instead of just pane is dead
a = input()