import os
import time
import random
import json
import glob

strFilePath = os.path.dirname(__file__) + '/WordLists/'

# Load the JSON Settings
with open(os.path.dirname(__file__) + '/Setting.json', 'r') as file:
    Settings = json.load(file)

# For Updating the Settings.json File, this will open both the Characters and Games Folders and add all txt in them to the settings
def funUpdatingSettings():
    txtCharacterFiles = glob.glob(os.path.join(strFilePath + "Characters/", '*.txt'))
    txtGamesFiles = glob.glob(os.path.join(strFilePath + "Games/", '*.txt'))
    
    for filepath in txtCharacterFiles:
       strFileName = os.path.basename(filepath)
       strSettingName = os.path.splitext(strFileName)[0]
       print(strSettingName)
       if strSettingName not in Settings["Character"]:
            Settings["Character"][strSettingName] = True
            
    for filepath in txtGamesFiles:
       strFileName = os.path.basename(filepath)
       strSettingName = os.path.splitext(strFileName)[0]
       if strSettingName not in Settings["Game"]:
            Settings["Game"][strSettingName] = True
    
    # Save the updated Settings
    with open(os.path.dirname(__file__) + '/Setting.json', 'w') as file:
        json.dump(Settings, file, indent=4)
 
# Changes all settings to true       
def funEverything2True():
    for key in Settings:
        Settings[key] = True

# Changes all settings to False (Note Please enable at least one before using as it will crash)        
def funEverything2False():
    for key in Settings:
        Settings[key] = False

funUpdatingSettings()
funEverything2True()