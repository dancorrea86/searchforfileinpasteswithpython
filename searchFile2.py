# coding: UTF-8
import os
import re

empresas = ['1000', '1001', '1002']
initialNumberCompanyes = 1002
ano = '2019'
mes = '06.2019'

my_dir = "./c-test-files/"


for dir, sub, files in os.walk(my_dir):
	if dir == (my_dir  + str(initialNumberCompanyes) + '/FISCAL/' + ano + '/' + mes + '/' + 'Declaração'):
		print (initialNumberCompanyes)
		print ('')
		for i in files:
			print (i)
		print ('*' * 100)
		print ('')
		initialNumberCompanyes -= 1

