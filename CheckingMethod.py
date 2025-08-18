import os
import time
import random

#Function Checks the letters in the quessed word and replaces them
def funCheckLetters(strGivenLetter = "", strWord = "", strQuessingWord = ""):
    strTemplist = list(strQuessingWord)
    intCountWhere = 0
    for char in strTemplist:
        if strWord[intCountWhere] == strGivenLetter:
            strTemplist[intCountWhere] = strGivenLetter
        intCountWhere += 1
    return "".join(strTemplist)

#Function Checks if the letter/number has already been guessedc
def funCheckQuesses(strLetter = "", strListOfLetters = []):
    intCountThrough = 0
    char = len(strListOfLetters)
    for char in strListOfLetters:
        if strListOfLetters[intCountThrough] == strLetter:
            return False
        intCountThrough +=1
    return True

#Function Checks to see if the user has ONLY put in 1 input
def funCheckForOneLetter(strQuess = ""):
    if len(strQuess) == 1:
        return True
    else:
        return False