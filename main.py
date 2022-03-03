from __future__ import print_function
import os
import sys


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
	print(text.renderText("LikeToAccess'"))
	text = Figlet(font="standard")
	print(text.renderText("name pending-inator"))

def readfile(file):
	with open(file, "r") as f:
		lines = f.read().split("\n")
		return lines

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
	files = chdir("SERVER OLD/definitions/spawn_groups")
	dir()
	for file in files:
		lines = readfile(file)
		print(f"\n{file}:")
		for line in lines:
			if "\"max_size\":" in line:
				max_size = line
			elif "\"entity_type\":" in line:
				entity_tpye = line
			if entity_tpye and max_size:
				print(f"{entity_tpye}\n{max_size}")

		# print("\n".join(file))



if __name__ == "__main__":
	intro()
	main()

