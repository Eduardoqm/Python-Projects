#Forest engine to generic forest simulator
#Eduardo Q Marques 08/01/2020

import os
import time

#Initial values -------------
#Vegetations variables
tree = int(100)
lit = int(25000)
nut = int(0)

#Everionment variables
mostair = int(100)
mosts = int(100)
temp = int(25)

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
    tempv = int(input('Temp variation (input +5 to -5): '))
    #mostairv = int(input('Air Moisture variation (input +10 to -10): '))
    
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
        temp = temp+tempv
        #mostair = mostair+mostairv
    
        lit = (tree*10)*temp
        nut = ((lit*mosts)/tree)/100

        mostair = (tree/100)*(temp*4)
        mosts = mostair+(tree/10)
        temp = (tree/temp)+temp

        morten = (nut/2)/tree
        tree = tree - morten 
