import re

lista = ["declaração", "gia", "nova Declaração", "SPED"]
pattern = '\declaração'

for i in lista:
	if re.search('eclaração', i):
		print (i)
