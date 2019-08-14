# -*- coding: utf-8 -*-
#Historia RPG parte-1 Versão "GOTO"
#@author: Eduardo Q Marques
#start=12/08/2019  Finnish=
from random import randint
   
def erro():
    print('COMANDO ERRADO!')

def dado():
    return randint(1,100)

def luta():

class person():

class inimigo():


while True:
    answer = input('Seguir na aventura? (sim/não)')
    if answer == 'sim':
        
        while True:
            answer = input('Você um é jovem da aldeia precisa sair e buscar alimento para sua família...\n'
                           'Ah duas opções... Seguir para a floresta ou para a vila. Qual você escolhe?\n')
            if answer == 'floresta':
                print('Você entrou na floresta')
                
                while True:
                    answer = input('Você quer seguir até o riacho ou até o precipicio da floresta?')
                    if answer == 'riacho':
                        print('Encontrou frutas silvestres parabéns')
                    elif answer == 'precipicio':
                        print('Você encontrou um guaxinim raivoso e agora terá que lutar pela sua vida!')
                        luta()
                    else:
                        erro()
                
            elif answer == 'vila':
                print('Você entrou na Vila')
                
            else:
                erro()
        
        
        
    elif answer == 'não':
        print('Volte outra hora para nos ajudar nessa aventura...abraço!!!\n'
		'by: EQM')
        break
    