#Spaceship Manage
#Eduardo Q Marques 10/01/2020

import os
import time

#Nave Runs
while True:
    os.system('cls')
    print('''
    Ship Locations
    -----------------------------------
    1-Mean Control room
    2-Life Machine room
    3-Storage room
    4-Computer room
    5-Machine room
    -----------------------------------

    ''')

    local = int(input('Choose a local: '))
    if local == 1:
        os.system('cls')
        print('''
        1-Navegation panel
        2-Computer panel
        3-Power panel
        4-Life conditions panel
        5-exit
        ''')

    elif local == 2:
        os.system('cls')
        print('''
        1-Oxigen generator
        2-Carbon filters
        3-Water recycler
        4-Temperature regulations
        5-exit
        ''')
    
    elif local == 3:
        os.system('cls')
        print('Need to put something')

    elif local == 4:
        os.system('cls')
        print('''
        1-Power regulators
        2-Distribution cables
        3-Hardware computer
        4-exit
        ''')
        res = int(input('Choose a piece: '))

        if res == 1:
            os.system('cls')
            print('''
            1-Swith off
            2-Restart
            3-Change fuse
            4-exit
            ''')

        elif res == 3:
            os.system('cls')
            print('''
            1-Processors
            2-Memories
            3-Hard Memory
            4-exit
            ''')
            
    elif local == 5:
        os.system('cls')
        print('''
        1-Propulsion Engine

        2-Correction Engine
        Pulse chambers cables
        Chambers selector
        Fuel general switch

        3-Power generators
        General switch
        Coolers
        Switch panel

        4-exit
        ''')    
