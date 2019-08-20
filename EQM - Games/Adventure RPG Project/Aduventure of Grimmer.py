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
#winsound.PlaySound('Abertura.wav', winsound.SND_ASYNC)

print("=========================================")
print("...........##............................")
print(".....########=========================>..")
print("...........##............................")
print("=========================================")
print("= --->    ADVENTURE OF GRIMMER    <---  =")
print("=           The last Wizard             =")
print("=========================================")
print("...........##............................")
print(".....########=========================>..")
print("...........##............................")
print("=========================================")
print(' ')
print("Todos os comandos devem ser ecritos em letra minusculas.")
print("Use sua imaginação!")
print(' ')
print('Capitulo- 1: Primeiro sobreviver, depois vingar-se!')
print(' ')
time.sleep(5)
#winsound.PlaySound('Intro.wav',winsound.SND_LOOP + winsound.SND_ASYNC)

#Important functions
def erro():
    print('COMANDO ERRADO!')

def d100():
    return randint(1,100)

#Player
def raiovital():
    if d100() >= 50:
        return randint(1,50)
    else: 
        return (0)
            
def fogo():
    if d100() >= 60:
        return randint(1,70)
    else:
        return (0)

#Sprites
def fraco():
    if d100() >= 55:
        return randint(1,30)
    else:
        return (0)

def medio():
    if d100() >= 40:
        return randint(1,70)
    else:
        return (0)

#Eventos
def luta1():
    winsound.PlaySound('batalha.wav',winsound.SND_LOOP + winsound.SND_ASYNC)
    vida = 100
    b = 100
    while True:
        poder = {
        '1': raiovital(),
        '2': fogo()
    }
        os.system('cls')
        print('========================\n'
            'Grimmer', vida,'%\n'
            '------------------------\n'
            'Inimigo=', b,'%\n'
            '========================\n'
            ' \n'
            'Tipo de ataque| Chance|Poder max|\n'
            '1-Raio Vital  |  50%  |   50    |\n'
            '2-Bola de fogo|  40%  |   70    |\n'
            ' \n')
        x = input('Escolha um comando: ')
        if x != '1' and x != '2':
            print('Comando ivalido!')
            time.sleep(1)
        else:
            b = b - poder[x]     
            vida = vida - fraco() 
            if vida < 1:
                winsound.PlaySound('morte.wav', winsound.SND_ASYNC)
                print('Você morreu!!!')
                print('Reinicie o jogo!')
                time.sleep(5000)
            
            elif b < 1:
                print('Você ganhou com', vida,'% de vida!')
                break
                
            else:
                time.sleep(1)
                
def luta2():
    winsound.PlaySound('batalha.wav',winsound.SND_LOOP + winsound.SND_ASYNC)
    vida = 100
    b = 100
    while True:
        poder = {
        '1': raiovital(),
        '2': fogo()
    }
        os.system('cls')
        print('========================\n'
            'Grimmer', vida,'%\n'
            '------------------------\n'
            'Inimigo=', b,'%\n'
            '========================\n'
            ' \n'
            'Tipo de ataque| Chance|Poder max|\n'
            '1-Raio Vital  |  50%  |   50    |\n'
            '2-Bola de fogo|  40%  |   70    |\n'
            ' \n')
        x = input('Escolha um comando: ')
        if x != '1' and x != '2':
            print('Comando ivalido!')
            time.sleep(1)
        else:
            b = b - poder[x]     
            vida = vida - fraco() 
            if vida < 1:
                winsound.PlaySound('morte.wav', winsound.SND_ASYNC)
                print('Você morreu!!!')
                print('Reinicie o jogo!')
                time.sleep(5000)
            
            elif b < 1:
                print('Você ganhou com', vida,'% de vida!')
                break
                
            else:
                time.sleep(1)

#The history
print('Nossa história começa em uma terra ainda habitada por seres mágicos\n'
       'e governada por reis subordinados a deuses amaldiçoados...')
print(' ')
time.sleep(2)
print('Esse é o ano 3103 de ARDAH...desde o ano 2700 é travada uma guerra\n'
      'pelo direito do uso da magia pelos humanos.\n'
      'Isso porque esses serem são considerados seres de casta baixa e não merecedores\n'
      'dos dons dos deuses...\n'
      'Nos últimos 330 anos do reino de SARANOVF foi dado o direito do uso da magia aos humanos.\n'
      'Esses apoiados por MUJICK, um deus de terceira geração que representava a saúde e a virtude\n'
      'e também o deus que mais tinha apreço pelos homens...\n'
      '...\n'
      'Porem uma guerra misteriosa entre os deuses foi travada no cosmos o que resultou no sumiço deles.\n'
      'Após 110 anos sem nenhum contato com os deuses monstros e outros seres magicamente mais poderosos\n'
      'que os humanos começaram a dominar ARDAH e consequentemente o reino de SARANOVF foi conquistada por um semideus...\n'
      'ANTAGANOUS filho de VULCAN o deus do fogo...\n'
      'ANTAGANOUS teve como primeiro ato de rei proibir a magia aos humanos e então escraviza-los!')             
print(' ')
time.sleep(2)
print('É aqui que tudo começa para você!\n'
      'Você é WANGUS GRIMMER. Um jovem adotado pelo mago de uma pequena vila do reino de SARANOVF...\n'
      'O nome desse mago é PRETON RINGO. Ele o encontrou quando ainda era um bebê e desde então o cria \n'
      'e ensina os dons da magia apesar de você não domina-la muito bem nem teórica nem praticamente!')                
time.sleep(2)                
while True:
    answer = input('Você deseja seguir na aventura? (sim/não)')
    if answer == 'sim':
        os.system('cls')
        print('Se quiser sair do jogo basta digitar "sair"')
        print(' ')
        time.sleep(2)
        while True:
            print('É madrugada e você escuta um barulho bem alto e um clarão de luz vindo da porta da sua casa...\n'
                           'E um ataque surpresa mandando pelo Rei para matar PETRON e você!')
            time.sleep(1)
            print('PETRON: Corra GRIMMER! Salve-se...eles são muitos mas eu posso segura-los! Pegue seu artefato magico vá e logo!')
            answer = input('Você vai fugir ou desobedecer lutar com o seu mestre?')
            if answer == 'lutar':
                print('Você resolve lutar e vai enfrentar um soldado...\n'
                      'Ele parece muito experiente e está armado com uma espada e você só têm um graveto magico\n'
                      'e duas magias em seu arsenal que podem falhar!')
                time.sleep(5)
                luta2()      
            elif answer == 'fugir':
                print('Você pula pela janela, mas da de cara com um soldado!...\n'
                      'Ele não parece muito experiente, mas está armado com uma velha espada e você só têm um graveto magico\n'
                      'e duas magias em seu arsenal que podem falhar!')
                time.sleep(5)
                luta1()
                        
                        
            elif answer == 'sair':
                break
            else:
                erro()
                
            
                    
        else:
            erro()
                   
    elif answer == 'não':
        print('Volte outra hora para nos ajudar nessa aventura...abraço!!!\n'
		'by: EQM')
        break
    
