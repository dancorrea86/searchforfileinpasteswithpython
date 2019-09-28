# coding: UTF-8
import os
import re

count_file = 0

dir1 = "/home/daniel/Programação/Projects/searchforfileinpasteswithpython/c-test-files/"

for path, sub, filenames in os.walk(dir1):
	if not path.endswith("__"):
		print ("Print Path: ", path)