#War Kaiser
#Eduardo Q Marques 10/01/2020

import os
import time
from random import randint

#Initial values -------------
money = int(2000000)
civ = int(8000)
sold = int(1950)
tsold = int(50)
tank = int(10)
rocket = int(3)
plane = int(2)

enemy = int(10000)

#Functions
def erro():
    print('COMANDO ERRADO!')

def d100():
    return randint(1,100)

def civfight():
    global enemy
    global civ
    if d100() >= 70:
        a = randint(30,40)
        enemy = enemy - a
        civ = civ - 25
        print('Your troop has won this battle!')
        print('{} soldiers enemies die...'.format(a))
        time.sleep(2)
    else: 
        b = randint(80,100)
        civ = civ - b
        print('Your troop has lost this battle!')
        print('{} soldiers die...'.format(b))
        time.sleep(2)

def soldfight():
    global enemy
    global sold
    if d100() >= 50:
        a = randint(30,50)
        enemy = enemy - a
        sold = sold - 20
        print('Your troop has won this battle!')
        print('{} soldiers enemies die...'.format(a))
        time.sleep(2)
    else: 
        b = randint(1,100)
        sold = sold - b
        print('Your troop has lost this battle!')
        print('{} soldiers die...'.format(b))
        time.sleep(2)

def tsoldfight():
    global enemy
    global tsold
    if d100() >= 40:
        a = randint(50,100)
        enemy = enemy - a
        tsold = tsold - 5
        print('Your troop has won this battle!')
        print('{} soldiers enemies die...'.format(a))
        time.sleep(2)
    else: 
        b = randint(1,100)
        tsold = tsold - b
        print('Your troop has lost this battle!')
        print('{} soldiers die...'.format(b))
        time.sleep(2)

def tankfight():
    global enemy
    global tank
    if d100() >= 35:
        a = randint(50,200)
        enemy = enemy - a
        print('Your tank has won this battle!')
        print('{} soldiers enemies die...'.format(a))
        time.sleep(2)
    else: 
        tank = tank - 1
        print('Your tank has been destroyed!')
        time.sleep(2)

def rockfight():
    global enemy
    global rocket
    if d100() >= 20:
        a = randint(200,500)
        enemy = enemy - a
        rocket = rocket - 1
        print('Your rocket has destroyed a base!')
        print('{} soldiers enemies die...'.format(a))
        time.sleep(2)
    else: 
        rocket = rocket - 1
        print('Your rocket has been intercepted!')
        time.sleep(2)

def planefight():
    global enemy
    global plane
    if d100() >= 20:
        a = randint(300,1000)
        enemy = enemy - a
        print('Your troop has won this battle!')
        print('{} soldiers enemies die...'.format(a))
        time.sleep(2)
    else: 
        plane = plane - 1
        print('Your airplane has been intercepted!')
        time.sleep(2)


country = input('The name of your country: ')
ecountry = input('The name of your enemy country: ')
#Logic engine
while True:
    people = sold+tsold+civ
    time.sleep(1)
    os.system('cls')
    print('-------------------------------{}------------------------------------'.format(country))
    print('''
    Money: {} | Population: {} |

    Soldiers: {} | Elite Soldiers: {}

    Tanks: {} | Rockets: {} | Airplanes: {}
    

    [ {} population: {} ]

    '''.format(money, people, sold, tsold, tank, rocket, plane, ecountry, enemy))

    order = int(input('''
    -----------------------------Orders---------------------------------
    1 - Attack
    2 - Make
    3 - Recruit

    Enter your order: '''))

    if people < 100:
        print('YOU LOST THE WAR!!!')
        time.sleep(600)

    elif order == 1:
        os.system('cls')
        atta = float(input('''
        1-Soldiers
        2-Elite Soldiers
        3-Tanks
        4-Rockets
        5-Airplanes
        6-No trainned force

        Enter your order: '''))

        if atta == 1:
            if sold >= 100:
                soldfight()
            else:
                print('You need more soldiers to make a troop...')

        elif atta == 2:
            if tsold >= 50:
                tsoldfight()
            else:
                print('You need more soldiers to make a troop...')

        elif atta == 3:
            if tank >= 1:
                tankfight()
            else:
                print('You need make a tank...')

        elif atta == 4:
            if rocket >= 1:
                rockfight()
            else:
                print('You need make a Rocket...')

        elif atta == 5:
            if plane >= 1:
                planefight()
            else:
                print('You need make a airplane...')

        elif atta == 6:
            if civ >= 100:
                civfight()
            else:
                print('You need more people to make a troop...')

        else:
            erro()

    elif order == 2:
        os.system('cls')
        make = float(input('''
        1-Tank
        2-Rocket
        3-Airplane

        Enter your order: '''))
        if make == 1:
            if money >= 100000:
                money = money - 100000
                tank = tank + 1
            else:
                print('Not enough money!!!')
        if make == 2:
            if money >= 150000:
                money = money - 150000
                rocket = rocket + 1
            else:
                print('Not enough money!!!')
        if make == 3:
            if money >= 300000:
                money = money - 300000
                plane = plane + 1
            else:
                print('Not enough money!!!')

    elif order == 3:
        os.system('cls')
        rec = float(input('''
        1-Soldier
        2-Elite Soldier

        Enter your order: '''))
        if rec == 1:
            if money >= 1000:
                money = money - 1000
                civ = civ - 100
                sold = sold + 100
            else:
                print('Not enough money!!!')
        if rec == 2:
            if money >= 1000 and sold >= 150:
                money = money - 1000
                sold = sold - 50
                tsold = tsold + 50
            else:
                print('Not enough solders or money!!!')
    else:
        erro()
