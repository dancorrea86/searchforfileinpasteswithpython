# coding: UTF-8
import os
import re

empresas = ['1000', '1001', '1002']
initialNumberCompanyes = 1000
ano = '2019'
mes = '06.2019'

my_dir = "S:\CLIENTES 2018"

for root, subFolders, files in os.walk(my_dir):
	print (subFolders)
	# subFolders.sort()
	# if root.startswith(my_dir + str(initialNumberCompanyes)) and root.endswith('/FISCAL/' + ano + '/' + mes + '/' + 'Declaração'):
		# print (initialNumberCompanyes)
		# print ('')
		# for i in files:
			# print (i)
		# print ('*' * 100)
		# print ('')
		# initialNumberCompanyes += 1