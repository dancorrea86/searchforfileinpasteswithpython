# coding: UTF-8
import os

my_dir = "/home/daniel/Programação/Projects/searchforfileinpasteswithpython/c-test-files"

for dir, sub, files in os.walk(my_dir):
	print ("Print Dir: ", dir) # print out each directory path
	sub = [n for n in sub] # print each sub folder in each dir
	contents = sub + files # sorst subs and files

	print (contents)
	for f in contents:
		if os.path.isfile(f):
			print ('\tJust The Files', f)
	print() # prints spaces between levels