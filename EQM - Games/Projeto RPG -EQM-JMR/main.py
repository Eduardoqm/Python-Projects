from random import randint
import os
# TEM DADO EM CASA?
def d4():
    return randint(1,4)

def d6():
    return randint(1,6)

def d8():
    return randint(1,8)

def d12():
    return randint(1,12)

def d20():
    return randint(1,20)

def ddt():
    return randint(30,100)

def d100():
    return randint(1,100)


#### MAGO
class Mago():

    def __init__(self,nome):
        self.nome = nome
        self.vida = 20
        self.__vida = 30

    def tiamat(self):
        if d100() >= 5:
            return d4()
        return False

    def raiovital(self):
        if d100() >= 10:
            return d6()
        return False

    def boladefogo(self):
        if d100() >= 25:
            return d12()
        return False

    def congelar(self):
        if d100() >= 15:
            return d8()
        return False

    def ficarinvisivel(self):
        if d100() >= 50:
            return 'inv'
        return False

    def autocura(self):
        if d100() >= 95:

            self.vida = self.vida + 15
            if self.__vida <= self.vida:
                self.vida = self.__vida
            return True
        return False

    def invocartiamat(self):
        if d100() >= 90:
            return ddt()
        return False

    def dano(self,dano):
        self.vida = self.vida - dano

    def is_vivo(self):
        if self.vida < 1:
            return False
        return True

    def __repr__(self):
        return f'Sou {self.nome} tenho {self.vida} pontos de vida' #Ver as live de python para aprender

# Dragao muito forte?
class Dragao():
    def __init__(self,nome):
        self.nome = nome
        self.vida = 50

    def ataque(self):
        if d100() >= 10:
            return d6()
        return False

    def dano(self,dano):
        self.vida = self.vida - dano

    def is_vivo(self):
        if self.vida < 1:
            return False
        return True


# Briga

edu = Mago('Gandof')
d = Dragao('Mongol')



msg = '';
while edu.is_vivo() and d.is_vivo():

    poder = {
        '1': edu.tiamat(),
        '2': edu.raiovital(),
        '4': edu.boladefogo(),
        '3': edu.congelar(),
        '5': edu.ficarinvisivel(),
        '6': edu.invocartiamat(),
        '7': True
    }

    # print(poder)
    os.system('cls')
    print('\n=========================================')
    print(' 1 Lagartixa Elétrica\n',
    '2 Raio Vital\n',
    '3 Congelar\n',
    '4 Bola de Fogo\n',
    '5 Invisibilidade\n',
    '6 Invocar Dragão Tiamat\n',
    '7 Auto Cura\n'
    '=========================================')
    print(f'{edu.nome} vida {edu.vida} | {d.nome} vida {d.vida} ')
    print(msg)
    msg = ''
    q = input('Escolha uma magia de 1 a 7\n')
    try:
        p = poder[q]
    except:
        p = False
    if p != False:
        if q != '7' and q != '5':
            d.dano(p)
            msg = msg + f'Causo {p} no {d.nome}\n'
        elif q == '5':
            msg = msg + 'Fico Invisivel\n'
        else:
            if edu.autocura():
                msg = msg + 'Se CUROU\n'
    else:
        msg = msg + 'Magia Falhou\n'

    if d.is_vivo():
        d_dano = d.ataque()
        if d_dano != False and p != 'inv':
            msg = msg + f'Você recebeu {d_dano}\n'
            edu.dano(d_dano)
        else:
            msg = msg + 'Dragao te errou\n'

print(f'{edu.nome} vida {edu.vida} | {d.nome} vida {d.vida} ')
if d.is_vivo():
    print('Você virou churrasco')
else:
    print('EEEE agora vai mata outro dragao')
