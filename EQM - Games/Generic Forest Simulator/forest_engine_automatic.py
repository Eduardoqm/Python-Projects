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
temp = float(25)

#Logic engine
while True:
    time.sleep(1)
    os.system('cls')
    print('-------------------------------CONTROL PANEL------------------------------------')
    print('''
    Trees: {} | Litter: {} | Nutrients per tree: {}
    Temperature: {}ºC | Air Moisture: {} | Soil Moisture: {}'''.format(tree, lit, nut, temp, mostair, mosts))
    print(' ')
    
    print('--------------------------------------------------------------------------------')
    print(' ')
    print('-----------------------------Ecossistem Command---------------------------------')
    #tempv = float(input('Temp Regulation (input +5 to -5): '))
    #mostairv = int(input('Air Moisture variation (input +10 to -10): '))
    
    if tree <= 0.0:
        print('The forest die...')
        time.sleep(2)
        print('GAME OVER!!!')
        time.sleep(5)
        
    elif temp > 40 and mostair < 40:
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
        tree = tree/2.5
        temp = 35

    elif temp > 40 and mosts < 50:
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
        tree = tree/1.7
        temp = 35

    elif temp >= 60:
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
        temp = 35

    else:
        #temp = temp+tempv
        #mostair = mostair+mostairv

        temp = float((5/tree)+temp)
        lit = (tree*10)*(temp/2)
        nut = (lit/tree)/100

        #Recruit and die
        morten = (100-((nut-100)+100))/75
        tree = tree - morten
        recruit = nut
        tree = tree+recruit

        mostair = tree - 5
        mosts = mostair+(tree/25)
