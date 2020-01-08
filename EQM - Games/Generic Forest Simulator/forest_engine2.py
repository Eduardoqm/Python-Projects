#Forest engine to generic forest simulator
#Eduardo Q Marques 08/01/2020

import os
import time

#Initial values -------------
#Vegetations variables
tree = float(100)
lit = float(25000)
nut = float(275)

#Everionment variables
mostair = float(100)
mosts = float(100)
temp = float(25)

#Logic engine
while True:
    time.sleep(1)
    os.system('cls')
    print('---------------------CONTROL PANEL--------------------------')
    print('''
    Trees: {} | Litter: {} | Nutrients: {}
    Temperature: {}ºC | Air Moisture: {} | Soil Moisture: {}'''.format(tree, lit, nut, temp, mostair, mosts))
    print(' ')
    
    print('------------------------------------------------------------')
    print(' ')
    print('-------------------Ecossistem Command-----------------------')
    tempv = float(input('Temp variation (input +2 to -2): '))
    mostairv = float(input('Air Moisture variation (input +10 to -10): '))
    temp = temp+tempv
    mostair = mostair+mostairv

    if temp > 40 and mostair < 40 and mosts < 50:
        os.system('cls')
        print('ALERT FIRE CONDITIONS ARE DETECTED!!!')
        time.sleep(1)
        print('ALERT FIRE CONDITIONS ARE DETECTED!!!')
        time.sleep(1)
        print('ALERT ECOSSITEM TILT!!!')
        time.sleep(2)
        print('''FIRE, FIRE, FIRE...
        Some trees will die!''')
        time.sleep(3)
        #mortef = (temp*lit)/100
        tree = tree/2

    elif tree <= 0:
        print('The forest die...')
        time.sleep(2)
        print('GAME OVER!!!')
        time.sleep(5)

    elif tree > 100:
        tree = int(100)
    
    else:
        lit = (tree*10)*temp
        nut = ((lit*mosts)/tree)/100

        mostair = (tree/100)*(temp*4)
        mosts = mostair+(tree/10)
        temp = tree/4

        morten = ((nut/2)/tree)/100
        tree = tree - morten 
