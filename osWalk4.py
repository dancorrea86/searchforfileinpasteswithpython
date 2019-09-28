# coding: UTF-8
import os

count_file = 0

dir1 = "/home/daniel/Programação/Projects/searchforfileinpasteswithpython/c-test-files/1000/FISCAL/2019/06.2019/Declaração/"

for path, sub, filenames in os.walk(dir1):
	print (sub)