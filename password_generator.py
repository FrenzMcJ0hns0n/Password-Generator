# -*- coding: utf-8 -*

import datetime
import random
from pathlib import Path


def ExitOnFatalError():
	print ("The program will exit now. Press Enter to continue ...")
	input()
	sys.exit(0)

def CheckFiles(file):
	characterFile = Path(file)
	if characterFile.is_file() == False:
		print ("Fatal error : File \"characters.txt\" not found !")
		ExitOnFatalError()
		
def LoadCharacters(file):
	fileReader = open(file, "r")
	string = ""
	for char in fileReader:
		string += char
	if string == "":
		print ("Fatal error : There isn't any character to load !")
		ExitOnFatalError()
	else:
		return string

def CheckUserInput():
	userInput = 0
	while 1:
		try:
			userInput = int(input("Desired length (2-20) : "))
		except ValueError:
			print("Error : Not an integer !")
			print("-------------------------")
			continue
		else:
			if userInput >= 2 and userInput <= 20:
				return userInput
			else:
				print("Error : Incorrect length !")
				print("-------------------------")

def WriteDateIntoFile(file):
	formattedDate = str(datetime.datetime.now().strftime('%d/%m/%Y-%Hh%M'))
	dateWriter = open(file, "a")
	dateWriter.write("\n===" + formattedDate + "===")
	dateWriter.close()

def BuildPassword(password_length, data):
	output = ""
	for x in range (0, password_length): 
		output += str(random.choice(data))
	return output

def WritePasswordIntoFile(file, text):
	textWriter = open(file, "a")
	textWriter.write("\n" + text)
	textWriter.close()


CheckFiles("characters.txt")
characters = LoadCharacters("characters.txt")
WriteDateIntoFile("text.txt")
print ("Possible characters :\n" + characters)
print("-------------------------")

while 1:
	chosenLength = CheckUserInput()
	password = BuildPassword(chosenLength, characters)
	WritePasswordIntoFile("text.txt", password)
	print ("Password : " + password)
	print("-------------------------")
