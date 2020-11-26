# -*- coding: utf-8 -*-
# filename          : main.py
# description       : Allows easy manipulation of various aspects of the game
# author            : LikeToAccess
# email             : liketoaccess@protonmail.com
# date              : 11-25-2020
# version           : v1.0
# usage             : python main.py
# notes             : For MCBE 1.16.100.04
# license           : MIT
# py version        : 3.7.8 (must run on 3.6 or higher)
#==============================================================================
from __future__ import print_function
import os
import sys

quantitative_multiplier = 2.0

try:
	from pyfiglet import Figlet
except ImportError as e:
	print(e)
	print("installing required modules...\n")
	os.system("pip install pyfiglet")

def clear():
	if sys.platform == 'win32': os.system("cls")
	else: os.system("clear")

def intro():
	clear()
	text = Figlet(font="slant")
	print(text.renderText("LikeToAccess' Minecraft Harder Mode"))

def readfile(file):
	with open(file, "r") as f:
		lines = f.read().split("\n")
		return lines

def writefile(file, data):
	with open(file, "w") as f:
		f.write(data)

def dir(directory=os.getcwd()):
	os.system("dir")

def listdir():
	files = os.listdir()
	# print(f"{os.getcwd()}>", end="")
	# print("dir\n{}".format("\n".join(files)))
	return files

def chdir(directory):
	os.chdir(directory)
	return listdir()

def main():
	home_dir = os.getcwd()
	new_data = []
	files = chdir("SERVER OLD/definitions/spawn_groups")
	dir()
	for file in files:
		lines = readfile(file)
		print(f"\n{file}:")
		for line in lines:
			entity_type = False
			if "\"max_size\":" in line:
				new_line = []
				chars = line
				for char in chars:
					try:
						char, old_size = int(float(char)*quantitative_multiplier), char
					except ValueError:
						pass
					finally:
						new_line.append(str(char))
				line = "".join(new_line)
				#print(line)
				max_size = line
			elif "\"entity_type\":" in line:
				entity_type = line
			if entity_type and max_size:
				entity_type = entity_type.strip("\"").replace("  ","").replace("\"entity_type\": \"minecraft:","")
				max_size = max_size.strip("\"").strip(",").replace("  ","").replace("\"max_size","").replace("\":",f"{old_size} ->")
				print("  {0}(s):\n    {1}".format(entity_type,max_size))
			new_data.append(line)
			#print(line)
	input("\nPress enter to continue:\n> ")

	intro()
	chdir(home_dir)
	files = chdir("SERVER NEW/definitions/spawn_groups")
	dir()
	for file in files:
		lines = readfile(file)
		print(f"\n{file}:")
		


if __name__ == "__main__":
	intro()
	main()

