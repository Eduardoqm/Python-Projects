#####################################
#     --> THE LEGEND OF EDD <--     #
#-----------------------------------#
#Adventure Game                     #
#EQM - GAMES                        #
#30/03/2019                         #
#Python                             #
#####################################
print("Todos os comandos devem ser ecritos em letra minusculas.")
print("Use sua imaginação!")
print("=========================================")
print("...........##............................")
print(".....##################################..")
print("...........##............................")
print("=========================================")
print("=  --->  THE LEGEND OF EDD  <---        =")
print("=        O ataque do dragão             =")
print("=========================================")
print("...........##............................")
print(".....##################################..")
print("...........##............................")

while True:
	answer = input ("Você escutou um barulho fora de casa. Você deseja verificar? (sim/não)")

	if answer.lower().strip() == "sim":

		answer = input("Você viu um dragão atacando sua vila...o que você vai fazer? (correr,lutar)").lower().strip()
		if answer == "lutar":
			answer = input("Você encontra uma besta e uma espada...oq ue você escolhe?")
			
			if answer == "espada":
				print("Não da para atacar um dragão de perto...você foi queimado vivo...GAME OVER!!!")
			else:
				print("Você atira a primeira seta mas ela apenas atinge o olho da fera!")
			
				answer = input("Você quer tentar outro tiro de besta ou quer tentar a espada? (espada, outro tiro)")
				
				if answer == "espada":
					print("Não da para atacar um dragão de perto...você foi queimado vivo...GAME OVER!!!")
				else:
					print("Milagrosamente você antige o dragão letalmente e todos em sua vila celebram! Você é um Heroi! PARABÉNS!!!")
			
		elif answer == "correr":
			print("Não da para correr de um dragão...você foi queimado vivo...GAME OVER!!!")
			
		else:
			print("Invalid coise, you lost!")
		
		
	else:
		print("Era um dragão atacando a seu vilareijo...ele queimou sua casa e você morreu...GAME OVER!!!")
		break