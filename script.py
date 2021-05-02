# script que combina duas wordlists

import sys
import os
from time import sleep as espere
# Use python3 script.py <senha> -2 ou -1 
# para dizer quantas wordlist você quer usar
os.system("clear")
arquivo = "senha1.txt"
arquivo2 = "senha2.txt"

def abrir_arquivo(arq,senha):
	encontrada = False
	file1 = open(arquivo, "rt")
	file2 = open(arquivo2, "rt")
	for x in file1:
		resultado = x.replace("\n","")
		print("\033[1;31mSenha: \033[m [{}] \033[1;31m[-]\033[m Não deu match!".format(resultado))
		if resultado == senha:
			print("=="*12)
			print("\n\033[1;32m[ MATCH ]\033[m SENHA ENCONTRADA: {} tempo para encontrar:\n".format(resultado))
			print("=="*12)
			encontrada = True
			sys.exit()
	print("\n\033[1;33m[INFO]\033[m Infelizmente não obtive resultado na wordlist1")
	print("\033[1;32m[!]\033[mTENTANDO ENCONTRAR A SUA SENHA COM A WORDLIST 2\n")
	espere(3)
	for l in file2:
		resultado2 = l.replace("\n","")
		print("\033[1;31mSenha: \033[m [{}]  \033[1;31m[-]\033[m Não deu match!".format(resultado2))
		if resultado2 == senha:
			print("=="*12)
			print("\n\033[1;32m[ MATCH ]\033[m SENHA ENCONTRADA: {}\n".format(resultado2))
			print("=="*12)
			encontrada = True
			sys.exit()	
	if encontrada == False:
		print("\033[1;32m[ UAU ]\033[m Parabéns! A sua senha é muito forte, utilizei duas wordlists e não encontrei!")


conec_script = sys.argv

if len(conec_script) == 2:
		senha = str(sys.argv[1])
		print("\033[1;32m[*]\033[m Tentando dar match na sua senha...")
		abrir_arquivo(arq=arquivo,senha=senha)
		
else:
	print("\033[1;33m[+]\033[m Use python3 script.py >senha aqui<")
	print("\n\033[1;33m[+]\033[m EXEMPLO: python3 script.py lucas")
