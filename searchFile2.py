# coding: UTF-8
import os
import re

count = 2

empresas = ['1000', '1001', '1002']
ano = '2019'
mes = '06.2019'

my_dir = "./c-test-files/"

for dir, sub, files in os.walk(my_dir):
	if dir == (my_dir  + empresas[count] + '/FISCAL/' + ano + '/' + mes + '/' + 'Declaração'):
		print (empresas[count])
		print (files)	
		print ('*' * 60)
		count -= 1



#/home/daniel/Programação/Projects/searchforfileinpasteswithpython/c-test-files/1000/FISCAL/2019/06/2019/Declaração
#/home/daniel/Programação/Projects/searchforfileinpasteswithpython/c-test-files/1000/FISCAL/2019/01.2019/Declaração