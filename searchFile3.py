# coding: UTF-8
import os
import re

empresas = ['1000', '1001', '1002']
initialNumberCompanyes = 1002
ano = '2019'
mes = '06.2019'

my_dir = "./c-test-files/"

arquivo = open('Relatorio.txt', 'w')

for dir, sub, files in os.walk(my_dir):
	print (dir.startswith(my_dir  + str(initialNumberCompanyes) + '/FISCAL/' + ano + '/' + mes + '/' + 'Declaração'))
	print (dir)
	print (my_dir  + str(initialNumberCompanyes) + '/FISCAL/' + ano + '/' + mes + '/' + 'Declaração')
	if dir.startswith(my_dir  + str(initialNumberCompanyes) + '/FISCAL/' + ano + '/' + mes + '/' + 'Declaração'):
		arquivo.write(str(initialNumberCompanyes)+'\n'+'\n')
		for i in files:
			arquivo.write(i+'\n')
		arquivo.write('*' * 100+'\n'+'\n')
		initialNumberCompanyes -= 1

arquivo.close()