#Spaceship Manage
#Eduardo Q Marques 10/01/2020

#Nave Runs
while True:
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
        print('''
        1-Navegation panel
        2-Computer panel
        3-Power panel
        4-Life conditions panel
        5-exit
        ''')

    elif local == 2:
        print('''
        Oxigen generator
        Carbon filters
        Water recycler
        Temperature regulations
        exit
        ''')
    
    elif local == 3:
        print('Need to put something')

    elif local == 4:
        print('''
        1-Power regulators
        2-Distribution cables
        3-Hardware computer
        ''')
        res = int(input('Choose a piece: ')

        if res == 1:
            print('''
            1-Swith off
            2-Restart
            3-Change fuse
            ''')

        elif res == 3:
            print('''
            1-Processors
            2-Memories
            3-Hard Memory
            ''')

        else:
            print('Back to map')

    elif local == 5:
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
        ''')    
