# coding: UTF-8
import os

count_file = 0

dir1 = "/home/daniel/Programação/Projects/searchforfileinpasteswithpython/c-test-files/"

for path, sub, filenames in os.walk(dir1):
	sub = [n for n in sub]
	content = sub + filenames

	for f in content:
		count_file += 1
		print ("Count: {} File Name: {}".format(count_file, f))