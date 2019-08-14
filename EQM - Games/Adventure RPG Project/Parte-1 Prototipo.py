# -*- coding: utf-8 -*-
#Historia RPG parte-1
#@author: Eduardo Q Marques
#start=12/08/2019  Finnish=

while True:
	answer = input ("Seguir na aventura? (sim/não)")

	if answer.lower().strip() == "sim":

		answer = input("Você sai de casa e encontra um senhor de idade e o nobre da vila na entrada do vilareijo...você precisa falar com um deles...(nobre,velho)").lower().strip()
		if answer == "velho":
			print("Velho: A floresta sabe tudo...o guardião é amigo dos coelhos...")
			answer = input("Entrar na vila ou seguir para a floresta?")
			if answer == "floresta":
				print("Você seguiu e entrou na floresta...")
				answer = input("Um lobo está atacando uma toca de coelhos...você deseja parar isso ou ignora? (parar, ignorar)")
				if answer == "ignorar":
					print("Você continua sua jorna ao centro da floresta...")
					print('Você segue mais um pouco e encontra o guardião da floresta...\n',
						'Eu me disfarcei de coelho e vc não me defendeu...era um teste evc não passou...terar que lutar comigo!!!')
				else:
					print("Você entra em uma batalha com o lobo!")
					
			else:
				answer = input("Você entrou na vila e ver 2 estabelecimentos que você pode pegar informações...Onde você vai?(Mercado ou Taberna)")
				if answer == "mercado":
					print("Dentro do mercado o comerciante pergunta: Vai comprar algo?...Você diz que não e sai...")
				else:
					print("Você pode sentar e pedir uma cerveja, Conversar com camponês bebado, Conversar com estrangeiro")
					
		elif answer == "nobre":
			print("Não posso falar com você agora...ah muito que se resolver na vila...")
		else:
			print("Invalid coise, you lost!")
		
		
	else:
		print('Volte outra hora para nos ajudar nessa aventura...abraço!!!\n'
		'by: EQM')
		break
