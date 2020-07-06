# -*- coding: utf-8 -*-
#Historia RPG parte-1 Versão "GOTO"
#@author: Eduardo Q Marques
#start=12/08/2019  Finnish=
from random import randint
import os
import time
import winsound
#import sys

os.chdir('C:\\Users\\Eduardo Q Marques\\Documents\\My Jobs\\Programas\\Python\\Python-Projects\\EQM - Games\\Adventure RPG Project\\Sounds')  
#winsound.PlaySound('picollo2.wav', winsound.SND_ASYNC)

print("=========================================")
print("...........##............................")
print(".....##################################..")
print("...........##............................")
print("=========================================")
print("= --->    Toy de teste do RPG     <---  =")
print("=        Uma aventura aleatória         =")
print("=========================================")
print("...........##............................")
print(".....##################################..")
print("...........##............................")
print("=========================================")
print("Todos os comandos devem ser ecritos em letra minusculas.")
print("Use sua imaginação!")
time.sleep(5)
#winsound.PlaySound('picollo2.wav',winsound.SND_LOOP + winsound.SND_ASYNC)

#Important functions
def erro():
    print('COMANDO ERRADO!')

def d100():
    return randint(1,100)

#Player
def soco():
    if d100() >= 20:
        return randint(1,50)
    else: 
        return (0)
            
def chute():
    if d100() >= 50:
        return randint(1,80)
    else:
        return (0)

#Sprites
def fraco():
    if d100() >= 70:
        return randint(1,20)
    else:
        return (0)

def medio():
    if d100() >= 40:
        return randint(1,70)
    else:
        return (0)

#Eventos
def luta1():
    vida = 100
    b = 100
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
        if x != '1' and x != '2':
            print('Comando ivalido!')
            time.sleep(1)
        else:
            b = b - poder[x]     
            vida = vida - fraco() 
            if vida < 1:
                print('Você morreu!!!')
                print('Reinicie o jogo!')
                time.sleep(5000)
            
            elif b < 1:
                print('Você ganhou com', vida,'% de vida!')
                break
                
            else:
                print('Novamente')
                time.sleep(1)
                
def luta2():
    vida = 100
    b = 100
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
        if x != '1' and x != '2':
            print('Comando ivalido!')
            time.sleep(1)
        else:
            b = b - poder[x]     
            vida = vida - medio() 
            if vida < 1:
                print('Você morreu!!!')
                print('Reinicie o jogo!')
                time.sleep(5000)
            
            elif b < 1:
                print('Você ganhou com', vida,'% de vida!')
                break
                
            else:
                print('Novamente')
                time.sleep(1)

#The history
while True:
    answer = input('Seguir na aventura? (sim/não)')
    if answer == 'sim':
        print('Se quiser sair do jogo basta digitar "sair"')
        while True:
            answer = input('Você um é jovem da aldeia precisa sair e buscar alimento para sua família...\n'
                           'Ah duas opções... Seguir para a floresta ou para a vila. Qual você escolhe?\n')
            if answer == 'floresta':
                print('Você entrou na floresta')
                
                while True:
                    answer = input('Você quer seguir até o riacho ou até a floresta densa?')
                    if answer == 'riacho':
                        print('Encontrou frutas silvestres parabéns!\n'
                              'Assim alimentou sua família!')
                        time.sleep(5000)
                    elif answer == 'floresta densa':
                        print('Você encontrou um guaxinim raivoso e agora terá que lutar pela sua vida!')
                        time.sleep(1)
                        luta1()
                        print('Você levou o guaxinim para casa e alimentou sua família!\n'
                              'Parabéns!!!')
                        time.sleep(5000)
                    elif answer == 'sair':
                        break
                    else:
                        erro()
                
            elif answer == 'vila':
                print('Você entrou na Vila')
                answer = input('Você entra na taverna ou revira o lixo?')
                if answer == 'taverna':
                    print('Você se envolve em uma briga!')
                    time.sleep(1)
                    luta2()
                    time.sleep(1)
                    print('Você viu que na vila não a nada para se alimentar!')
                elif answer == 'lixo':
                        print('Você encontrou um rato e ele está te atacando!')
                        time.sleep(1)
                        luta1()
                        time.sleep(1)
                        print('Você viu que na vila não a nada para se alimentar!')
                elif answer == 'sair':
                    break
                else:
                    erro()
                    break
                
            elif answer == 'sair':
                break
                    
        else:
            erro()
                   
    elif answer == 'não':
        print('Volte outra hora para nos ajudar nessa aventura...abraço!!!\n'
		'by: EQM')
        break
    