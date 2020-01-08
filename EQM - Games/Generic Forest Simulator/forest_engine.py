#Forest engine to generic forest simulator
#Eduardo Q Marques 08/01/2020

#Initial values -------------
#Vegetations variables
tree = int(100)
lit = int(25000)
nut = int(27500)

#Everionment variables
mostair = int(100)
mosts = int(100)
temp = int(25)

#Logic engine
while True:
    tempv = int(input('Temp variation (input +2 to -2): '))
    mostairv = int(input('Air Moisture variation (input +10 to -10): '))
    temp = tempv+temp
    mostair = mostairv+mostair

    if temp > 40:
        print('fire')
        mortef = (temp*lit)/100
        tree = mortef - tree

    else:
        tronc = 100 - tree
        lit = (tree*10)*temp
        nut = (lit*mosts)/tree

        mostair = (tree/100)*(temp*4)
        mosts = mostair+10
        temp = tree/4

        morten = ((nut/2)/tree)100
        tree = morten - tree