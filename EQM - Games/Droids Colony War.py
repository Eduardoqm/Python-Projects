from random import randint
import os

#Probabilidades de dados
def d100():
    return randint(1,100)

def d500():
    return randint(10,500)

def d1000():
    return randint(10,1000)
	
def d51():
    return randint(500,1000)

def d24():
    return randint(2000,4000)

def d48():
    return randint(4000,8000)
	
	
	
#Droid colony
#Missel de fissão R10   P5  D4000-8000
#Missel massivo   R50   P10 D2000-4000
#Missel thunder   R100  P50 D10-1000
#Ataque aereo     R200  P70 D10-1000
#Mega Droids      R200  P50 D500-1000
#Droids troops    R1000 P70 D500-1000
#Droids isolated  R500  P90 D10-500
#Recurso 10000
class Droid():

    def __init__(self,nome):
        self.nome = nome
        self.vida = 10000
        self.__vida = 30

    def nd(self):
        if d100() >= 99:
            return d500()
        return False
		
    def di(self):
        if d100() >= 10:
            return d500()
        return False

    def dt(self):
        if d100() >= 30:
            return d51()
        return False

    def md(self):
        if d100() >= 50:
            return d51()
        return False

    def aa(self):
        if d100() >= 30:
            return d1000()
        return False

    def mt(self):
        if d100() >= 50:
            return d1000()
        return False

    def mm(self):
        if d100() >= 90:
            return d24()
        return False

    def mf(self):
        if d100() >= 95:
            return d48()
        return False

    def dano(self,dano):
        self.vida = self.vida - dano

    def is_vivo(self):
        if self.vida < 1:
            return False
        return True

    def __repr__(self):
        return f'Sou {self.nome} tenho {self.vida} pontos de vida'
		
#Colonia inimiga
class Enemy():
    def __init__(self,nome):
        self.nome = nome
        self.vida = 10000

    def ataque(self):
        if d100() >= 50: #probabilidade do ataque dar certo
            return d1000() #potencia do ataque
        return False

    def dano(self,dano):
        self.vida = self.vida - dano

    def is_vivo(self):
        if self.vida < 1:
            return False
        return True
		
#Motor da luta

edu = Droid('LINUX-Colony')
d = Enemy('DOS-Colony')



msg = '';
while edu.is_vivo() and d.is_vivo():

    poder = {
		'0': edu.nd(),
        '1': edu.di(),
        '2': edu.dt(),
        '4': edu.md(),
        '3': edu.aa(),
        '5': edu.mt(),
        '6': edu.mm(),
        '7': edu.mf()
    }

    # print(poder)
    os.system('cls')
    print('\n===================================================')
    print(' 1 Droids de Reconhecimento (90%)\n',
    '2 Droids troop (70%)\n',
    '3 Mega Droids (50%)\n',
    '4 Ataque Air Droids (70%)\n',
    '5 Missel Thunder (50%)\n',
    '6 Missel Massivo (10%)\n',
    '7 Missel de Fissão (5%)\n'
    '===================================================')
    print(f'{edu.nome} vida {edu.vida} | {d.nome} vida {d.vida} ')
    print(msg)
    msg = ''
    q = input('Escolha uma ação de 1 a 7\n')
    try:
        p = poder[q]
    except:
        p = False
    if p != False:
        if q != '0' and q != '0':
            d.dano(p)
            msg = msg + f'Causou {p} no {d.nome}\n'
        elif q == '0':
            msg = msg + 'Fico Invisivel\n'
        else:
            if edu.autocura():
                msg = msg + 'Se CUROU\n'
    else:
        msg = msg + 'Ataque falhou!\n'

    if d.is_vivo():
        d_dano = d.ataque()
        if d_dano != False and p != 'inv':
            msg = msg + f'Você recebeu {d_dano}\n'
            edu.dano(d_dano)
        else:
            msg = msg + 'Te errou\n'

print(f'{edu.nome} recurso {edu.vida} | {d.nome} recurso {d.vida} ')
if d.is_vivo():
    print('SUA COLÔNIA FOI DESTRUIDA...GAME OVER!!!')
else:
    print('VOCÊ VENCEU A GUERRA DAS CYBER COLÔNIAS!!!')
