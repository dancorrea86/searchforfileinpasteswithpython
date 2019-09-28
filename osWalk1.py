# coding: UTF-8
import os

my_dir = "/home/daniel/Programação/Projects/searchforfileinpasteswithpython/c-test-files"

# intro  to os.walk
print("*************Star print**********")
for root_dir_path, sub_dirs, files in os.walk(my_dir):
	print ("Root Directory Path: ", root_dir_path)
	print ("Sub Directories: ", sub_dirs)
	print ("Files", files)
	print ("*" * 25)
print("*************End print**********")