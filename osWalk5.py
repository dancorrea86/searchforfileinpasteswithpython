# coding: UTF-8
import os
import re

count_file = 0

dir1 = "/home/daniel/Programação/Projects/searchforfileinpasteswithpython/c-test-files/"

for path, sub, filenames in os.walk(dir1):
	sub = [n for n in sub]
	content = sub + filenames
	
	for f in content:
		if re.search('[Gia]', str):
			print('Print Path ', path)