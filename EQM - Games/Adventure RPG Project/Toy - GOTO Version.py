# -*- coding: utf-8 -*-
#Historia RPG parte-1 Versão "GOTO"
#@author: Eduardo Q Marques
#start=12/08/2019  Finnish=
from random import randint
import os
import time
  
#Important functions
def erro():
    print('COMANDO ERRADO!')

#Player
def soco():
    return randint(0,20)

def chute():
    return randint(0,30)

#Sprites
def fraco():
    return randint(0,10)

def medio():
    return randint(0,30)

#Pixel art
def morte():
    print('[x J x]\n'
          ' |[O]|')

#Eventos
def luta1():
    vida = 100
    b = 100
    
    #Motor de batalha
    while True:
        poder = {
        '1': soco(),
        '2': chute()
    }
        os.system('cls')
        print('========================\n'
            'Sua vida=', vida,'%\n'
            '------------------------\n'
            'Vida do inimigo=', b,'%\n'
            '========================\n'
            '1-soco\n'
            '2-chute')
        x = input('Escolha um comando: ')
            
        b = b - poder[x]     
        vida = vida - fraco() 
        if vida < 1:
            print('Você morreu!!!')
            print('Reinicie o jogo!')
            morte()
            time.sleep(500)
        
        elif b < 1:
            print('Você ganhou com', vida,'% de vida!')
            break
            
        else:
            time.sleep(1)
            
def luta2():
    vida = 100
    b = 100
    
    #Motor de batalha
    while True:
        poder = {
        '1': soco(),
        '2': chute()
    }
        os.system('cls')
        print('========================\n'
            'Sua vida=', vida,'%\n'
            '------------------------\n'
            'Vida do inimigo=', b,'%\n'
            '========================\n'
            '1-soco\n'
            '2-chute')
        x = input('Escolha um comando: ')
            
        b = b - poder[x]     
        vida = vida - medio() 
        if vida < 1:
            print('Você morreu!!!')
            print('Reinicie o jogo!')
            morte()
            time.sleep(500)
        
        elif b < 1:
            print('Você ganhou com', vida,'% de vida!')
            break
            
        else:
            time.sleep(1)

#The history
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
                        time.sleep(1)
                        luta1()
                    else:
                        erro()
                
            elif answer == 'vila':
                print('Você entrou na Vila')
                answer = input('Você entra na taverna ou revira o lixo?')
                if answer == 'taverna':
                    print('Você se envolve em uma briga!')
                    time.sleep(1)
                    luta2()
                elif answer == 'lixo':
                        print('Você encontrou um rato e ele está te atacando!')
                        time.sleep(1)
                        luta1()
                else:
                    erro()
                        
            else:
                erro()
                break
        
        
        
    elif answer == 'não':
        print('Volte outra hora para nos ajudar nessa aventura...abraço!!!\n'
		'by: EQM')
        break
    