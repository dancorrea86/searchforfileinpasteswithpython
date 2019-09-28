import os

my_dir = "/home/daniel/Programação/Projects/searchforfileinpasteswithpython/c-test-files"

for dir, sub, files in os.walk(my_dir):
	print ("Print Dir: ", dir) # print out each directory path
	sub = [n for n in sub] # print each sub folder in each dir
	sub.sort()

	for f in sub:
		print('\tJust The Subs ', f)
	print()