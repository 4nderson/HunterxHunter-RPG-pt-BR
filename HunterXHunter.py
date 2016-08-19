#Script para jogar RPG hunter hunter, mais bem trabalhado e com o codigo melhorado!
#Ainda nao finalizado!
#Escrito por Anderson Leite

import time
import os



######Sistema de batalha#####
def tipo_luta(vida,atk,speed,destreza,resistencia,contador,inimigo_life):
	if contador ==1:
		tipo = input("Qual o tipo de ataque agora? \n N(Normal) A.B(Arma Branca) A.F(Arma de fogo):\n> ")
	else:
		tipo = input("Qual o tipo de luta voce deseja? \n N(Normal) A.B(Arma Branca) A.F(Arma de fogo):\n> ")
	if tipo == "N" or tipo == "Normal" or tipo == "n":
		print("Vamos la!")
		os.system("clear")
		contador = 2
		normal(vida,atk,speed,resistencia,destreza,inimigo_life)
	if tipo == "A.B" or tipo == "Arma Branca" or tipo == "ab" or tipo == "AB":
		print("Vamos la!")
		os.system("clear")
		arma_branca(vida,atk,speed,destreza,resistencia,inimigo_life)
	if tipo == "A.F" or tipo =="Arma de fogo" or tipo == "AF" or tipo == "af":
		print("Vamos la!")
		os.system("clear")
		normal(vida,atk,speed,destreza,resistencia,inimigo_life)
def normal(vida,atk,speed,destreza,resistencia,life):
	dano = atk + speed
	bonus = input("Teve bonus de ataque? Se sim, de quanto? \n> ")
	if bonus > 0:
		bonus += 0
	elif bonus == "n" or bonus == "nao" or bonus == "":
		bonus = 0
	if life > 0:
		life += 0
	else:
		life = input("Qual a vida do inimigo?\n> ")
	life += -dano
	print("Dano de %d,  inimigo agora com %d" %(dano,life))
	if life == 0 or life < 0:
		print("Inimigo derrotado!")
		print("Saindo...")
		time.sleep(0.3)
		os.system("clear")
		espera(vida)
	elif life > 0 or life != 0:
		atk_inimigo(vida,atk,speed,destreza,resistencia,life)
def atk_inimigo(vida,at,speed,destreza,resistencia,life):
	atk = input("De quanto foi o ataque do inimigo?")
	vida += -atk
	print("Dano de %d, sua vida agora é %d" % (atk, vida))
	contador = 1
	tipo_luta(vida,atk,speed,destreza,resistencia,contador,life)


########CRIANDO E LENDO O SAVE######



######Declarando funçoes/variaveis

def ficha(nome,idade,olhos,Peso,cabelos,altura,sexo,level,aucunha,personalidade,historia,aparencia,Talento_1,Talento_2,Talento_3,Pericia_1,Pericia_2,Pericia_3,Pericia_4,Pericia_5,Estilo,descri, HP, Nem, force, agil, destr,speed,intel, resistencia, fogo, Armas ):
	print("\nNome:%s \t Level: %s" % (nome,level))
	print("\nIdade: %s \t Peso: %s \t Altura: %s \t Sexo: %s" % (idade,Peso,altura,sexo))
	if cabelos == "":
		print("")
	else:
		print("Cabelos %s" % cabelos)
	if aucunha == "":
		print("")
	else:
		print("\nAlcunha: %s " % aucunha)
	if personalidade == "":
		print("")
	else:
		print("Personalidade:\n ---> %s" % (personalidade))
	if historia == "":
		print("")
	else:	
		print("Historia:\n ---- >%s" %(historia))
	if aparencia == "":
		print("")
	else:
		print("\t\t\nAparência:\n --- > %s" % (aparencia))	
	print("\n")
	atributos(Talento_1,Talento_2,Talento_3,Pericia_1,Pericia_2,Pericia_3,Pericia_4,Pericia_5,Estilo,descri, HP, Nem, force, agil, destr,speed,intel, resistencia, fogo, Armas )
def atributos(Talento_1, Talento_2, Talento_3, Pericia_1, Pericia_2, Pericia_3,Pericia_4,Pericia_5,Estilo_de_luta,Descrissao_de_tecnicas,HP,Nen,force,agilidade,destreza,speed,inteligencia,resitencia,poder_de_fogo, Armas):
	print("Talento 1:\t Pontos de Vida: %s \n \t \n \tPontos de Nen: %s \n %s \n" % (HP, Nen, Talento_1))
	print("Talento 2:\t Força: %s \n \t \tAgilidade: %s \n\t \tDestreza:  %s \n\t \tVelocidade: %s \n\t \tInteligencia: %s \n %s \n " % (force,agilidade,destreza,speed,inteligencia,Talento_2))
	print("Talento 3:\t Resistencia: %s \n \t \tPoder de fogo: %s \n %s \n" % (resitencia,poder_de_fogo,Talento_3))
	print("Pericia 1:\n %s \n" % Pericia_1)
	print("Pericia 2:\n %s \n" % Pericia_2)
	print("Pericia 3:\n %s \n"% Pericia_3)
	print("Pericia 4:\n %s \n"% Pericia_4)
	print("Pericia 5:\n %s \n" % Pericia_5)
	print("Estilo de luta:\n %s \n"% Estilo_de_luta)
	print("Descrição e Tecnicas:\n %s \n" % Descrissao_de_tecnicas)
	print("\t\tArmas utilizadas:\n %s" % Armas)
	print("Sua ficha ficou salvo em 'ficha.txt'\n")
	batalha = input("Preparado para batalha?(S/N)")
	if batalha == "S" or batalha == "s":
		inimigo_life = 0
		contador = 0
		print("Go!")
		os.system("clear")
		tipo_luta(HP,force,speed,destreza,resitencia,contador,inimigo_life)



###PREENCHIMENTO DE DADOS COM AS VARIAVEIS E APRESENTAÇÃO DO SCRIPT AO CLIENTE

def main():
	os.system("touch savemgame.txt")
	print("olá!")
	time.sleep(0.3)
	print(":)")
	time.sleep(0.1)
	os.system("clear")
	savegame = open("savegame.txt", "a")
	print("\t#Seja bem vindo ao script para jogar o RPG de HUNTERxHUNTER!")
	print("\n\t$Script em testes sujeito a bugs!!\n")
	print("\n\tVamos preencher sua ficha!\n \tEnjoy :) ")
	nome = input("\nQual o nome do seu personagem?\n> ")
	savegame.write("%s\n" %(nome))
	idade = input("\nQual a idade?\n> ")
	savegame.write("%s\n" %(idade))
	olhos = input("\nQual a cor dos olhos?\n >  (opcional)") 
	savegame.write("%s\n" %(olhos))
	peso = input("\nQual o peso?\n> ")
	savegame.write("%s\n" %(peso))
	cabelos = input("\nQual o cabelo? (opcional) \n> ")
	savegame.write("%s\n" %(cabelos))
	altura = input("\nQual a altura?(opcional) \n> ")
	savegame.write("%s\n" %(altura))
	sexo = input("\nQual o sexo?\n > ")
	savegame.write("%s\n" %(sexo))
	level = input("\nQual o level?\n >")
	savegame.write("%s\n" %(level))
	aucunha = input("\nQual a sua alcunha?\n > (característica particular física ou moral)")
	savegame.write("%s\n" %(aucunha))
	personalidade = input("\nQual a sua personalidade? (opcional) \n> ")
	savegame.write("%s\n" %(personalidade))
	historia = input("\nQual a sua historia?\n> (recomendado)")
	savegame.write("%s\n" %(historia))
	aparencia = input("\nQual a sua aparencia?\n> (opcional)")
	savegame.write("%s\n" %(aparencia))
	print("\nOk, basico preenchido!, vamos la!")
	print("Vamos agora preencher Seus atributos físicos!\n> ")
	os.system("clear")
	Talento_1 = input("Qual o seu primeiro talento?\n> \n")
	savegame.write("%s\n" %(Talento_1))
	Talento_2 = input("Qual o seu segundo talento?\n > \n")
	savegame.write("%s\n" %(Talento_2))
	Talento_3 = input("Qual o seu terceiro talento?\n > \n")
	savegame.write("%s\n" %(Talento_3))
	Talento_4 = input("Qual o seu quarto talento?\n > \n")
	savegame.write("%s\n" %(Talento_4))
	Pericia_1 = input("Qual a sua primeira pericia?\n> \n")
	savegame.write("%s\n" %(Pericia_1))
	Pericia_2 = input("Qual a sua segunda pericia?\n > \n")
	savegame.write("%s\n" %(Pericia_2))
	Pericia_3 = input("Qual a sua terceria pericia?\n > \n")
	savegame.write("%s\n" %(Pericia_3))
	Pericia_4 = input("Qual a sua quarta pericia?\n > \n")
	savegame.write("%s\n" %(Pericia_4))
	Pericia_5 = input("Qual a sua quinta pericia?\n > \n")
	savegame.write("%s\n" %(Pericia_5))
	Estilo = input("Qual o seu estilo de luta?\n > \n")
	savegame.write("%s\n" %(Estilo))
	descri = input("Fale sobre seu estilo de luta e Tecnicas:\n> ")
	savegame.write("%s\n" %(descri))
	HP = input("Qual a sua vida?\n > ")
	savegame.write("%s\n" %(HP))
	Nem = input("Quanto é o seu Nen? (caso não tenha, deixe em branco)\n>")
	if Nem == "":
		Nem = 0
		savegame.write("%s\n" %(Nem))
	else:
		savegame.write("%s\n" %(Nem))
	force = input("De quanto é a sua força?\n > \n")
	savegame.write("%s\n" %(force))
	agil = input("De quanto é a sua agilidade?\n > \n")
	savegame.write("%s\n" %(agil))
	destr = input("De quanto é a sua destreza? \n > \n")
	savegame.write("%s\n" %(destr))
	speed = input("De quanto é a sua velociade?\n > \n")
	savegame.write("%s\n" %(speed))
	intel = input ("De quanto é a sua inteligencia?\n> \n")
	savegame.write("%s\n" %(intel))
	resistencia = input("De quanto é a resistencia?\n > \n")
	savegame.write("%s\n" %(resistencia))
	fogo = input("\nDe quanto é o seu poder de fogo?\n > \n")
	savegame.write("%s\n" %(fogo))
	Armas = input("Quais as suas armas?\n> ")
	savegame.write("%s\n" %(Armas))
	savegame.write("\n")
	savegame.close()
	print("\nTudo preenchido!, vamos la!")
	save = input("Voce deseja salvar?(S/N)\n> ")
	if save == "S" or save =="Sim" or save == "s":
		print("Salvando...")
		time.sleep(0.2)
		print("Salvo com sucesso em 'savegame.txt'\n :)\n Não trapaceie modificando seu save :)\n")
	else:
		print("Tudo bem, prosseguindo com o jogo...")
		os.system("rm savegame.txt")
		os.system("touch savegame.txt")
	print(".")
	time.sleep(0.3)
	print("..")
	time.sleep(0.3)
	print("...")
	time.sleep(0.3)
	os.system("clear")
	os.system("clear")
	


	ficha(nome,idade,olhos,peso,cabelos,altura,sexo,level,aucunha,personalidade,historia,aparencia,Talento_1,Talento_2,Talento_3,Pericia_1,Pericia_2,Pericia_3,Pericia_4,Pericia_5,Estilo,descri, HP, Nem, force, agil, destr,speed,intel, resistencia, fogo, Armas )
main()
	



#FAZER OS SAVES FUNCIONAR E FAZER O SISTEMA DE BATALHA!, QUASE LA! :)




			
