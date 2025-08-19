import os
import time
import random
import json
import glob

strFilePath = os.path.dirname(__file__) + '/WordLists/'

# Load the JSON Settings
with open(os.path.dirname(__file__) + '/Setting.json', 'r') as file:
    Settings = json.load(file)

def funUpdatingSettings():
    txtCharacterFiles = glob.glob(os.path.join(strFilePath + "Characters/", '*.txt'))
    txtGamesFiles = glob.glob(os.path.join(strFilePath + "Games/", '*.txt'))
    
    for filepath in txtCharacterFiles:
       strFileName = os.path.basename(filepath)
       strSettingName = os.path.splitext(strFileName)[0]
       print(strSettingName)
       if strSettingName not in Settings["Character"]:
            Settings["Character"][strSettingName] = False
            
    for filepath in txtGamesFiles:
       strFileName = os.path.basename(filepath)
       strSettingName = os.path.splitext(strFileName)[0]
       if strSettingName not in Settings["Game"]:
            Settings["Game"][strSettingName] = False
    
    # Save the updated Settings
    with open(os.path.dirname(__file__) + '/Setting.json', 'w') as file:
        json.dump(Settings, file, indent=4)
        
def funEverything2True():
    for key in Settings:
        Settings[key] = True
        
def funEverything2False():
    for key in Settings:
        Settings[key] = False

funUpdatingSettings()