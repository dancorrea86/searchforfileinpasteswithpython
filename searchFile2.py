# coding: UTF-8
import os
import re

count = 2

empresas = ['1000', '1001', '1002']
ano = '2019'
mes = '06.2019'

my_dir = "/home/daniel/Programação/Projects/searchforfileinpasteswithpython/c-test-files/"

for dir, sub, files in os.walk(my_dir):
	if dir == (my_dir  + empresas[count] + '/FISCAL/' + ano + '/' + mes + '/' + 'Declaração'):
		print (empresas[count])
		print (files)	
		print ('*' * 60)
		count -= 1

