# -*- coding: utf-8 -*

import datetime
import random
from pathlib import Path

def ExitOnError():
	""" Simply displays a message, then quit """
	print ("The program will exit now. Press Enter to continue ...")
	input()
	sys.exit(0)

def CheckFiles(file):
	""" Checks if the specified file really exists in the current working directory """
	characterFile = Path(file)
	if characterFile.is_file() == False:
		print ("Fatal error : File \"characters.txt\" not found !")
		ExitOnError()

def LoadCharacters(file):
	""" Returns a string which contains the characters loaded from the file 'characters.txt' """
	fileReader = open(file, "r")
	string = ""
	for char in fileReader:
		string += char
	if string == "":
		print ("Fatal error : There isn't any character to load !")
		ExitOnError()
	else:
		return string

def CheckUserInput():
	""" Verifies if the user's input is matching expectations, then returns an integer """
	userInput = 0
	while True:
		try:
			userInput = int(input("Desired length (2-20) : "))
		except ValueError:
			print("Error : Not an integer !")
			print("-------------------------")
			#continue
		else:
			if userInput >= 2 and userInput <= 20:
				return userInput
			else:
				print("Error : Incorrect length !")
				print("-------------------------")

def WriteDateIntoFile(file):
	""" Writes the current time and date in french format into the output file """
	formattedDate = str(datetime.datetime.now().strftime('%d/%m/%Y-%Hh%M'))
	with open(file, 'a') as dateWriter:
		dateWriter.write("\n===" + formattedDate + "===")

def BuildPassword(password_length, data):
	""" Buils a password from 'data' using the length chosen by the user """
	output = ""
	for x in range (0, password_length):
		output += str(random.choice(data))
	return output

def WritePasswordIntoFile(file, text):
	""" Writes the built password into the output file """
	with open(file, 'a') as textWriter:
		textWriter.write("\n" + text)


CheckFiles("characters.txt")
characters = LoadCharacters("characters.txt")
WriteDateIntoFile("text.txt")
print ("Possible characters :\n" + characters)
print("-------------------------")

while True:
	chosenLength = CheckUserInput()
	password = BuildPassword(chosenLength, characters)
	WritePasswordIntoFile("text.txt", password)
	print ("Password : " + password)
	print("-------------------------")
