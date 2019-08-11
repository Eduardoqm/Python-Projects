from random import randint
import os
# Dados de probabilidade
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


#Player (Submarino)
class SubmarinoA():

    def __init__(self,nome):
        self.nome = nome
        self.vida = 100
        self.__vida = 50

    def torpedo04(self):
        if d100() >= 5:
            return d4()
        return False

    def torpedo012(self):
        if d100() >= 25:
            return d12()
        return False

    def torpedo08(self):
        if d100() >= 15:
            return d8()
        return False

    def autocura(self):
        if d100() >= 70:

            self.vida = self.vida + 40
            if self.__vida <= self.vida:
                self.vida = self.__vida
            return True
        return False

    def dano(self,dano):
        self.vida = self.vida - dano

    def is_vivo(self):
        if self.vida < 1:
            return False
        return True

    def __repr__(self):
        return f'Sou {self.nome} tenho {self.vida} pontos de vida'

#Submarino inimigo
class SubmarinoB():
    def __init__(self,nome):
        self.nome = nome
        self.vida = 30 #vida do inimigo

    def ataque(self):
        if d100() >= 30: #chance do inimigo te acertar
            return d4() #Maximo de dano que o inimigo pode te causar
        return False

    def dano(self,dano):
        self.vida = self.vida - dano

    def is_vivo(self):
        if self.vida < 1:
            return False
        return True


#Motor de batalha

edu = SubmarinoA('URSS')
d = SubmarinoB('USA')



msg = '';
while edu.is_vivo() and d.is_vivo():

    poder = {
        '1': edu.torpedo04(),
        '2': edu.torpedo08(),
        '3': edu.torpedo012(),
        '4': True
    }

    # print(poder)
    os.system('cls')
    print('\n=========================================')
    print(' 1 Torpedo pequeno-04 (95%)\n',
    '2 Torpedo medio-08 (85%)\n',
    '3 Torpedo grande-012 (75%)')
    print('=========================================')
    print(f'{edu.nome} vida {edu.vida} | {d.nome} vida {d.vida} ')
    print('=========================================')
    print(msg)
    msg = ''
    q = input('Escolha um comando de 1 a 3\n')
    try:
        p = poder[q]
    except:
        p = False
    if p != False:
        if q != '4' and q != '5':
            d.dano(p)
            msg = msg + f'Causo {p} no {d.nome}\n'
        elif q == '5':
            msg = msg + 'Fico Invisivel\n'
        else:
            if edu.autocura():
                msg = msg + 'fez um reparo de emergência\n'
    else:
        msg = msg + 'Ação sem sucesso\n'

    if d.is_vivo():
        d_dano = d.ataque()
        if d_dano != False and p != 'inv':
            msg = msg + f'Você recebeu {d_dano}\n'
            edu.dano(d_dano)
        else:
            msg = msg + 'Submarino inimigo te errou\n'

print(f'{edu.nome} vida {edu.vida} | {d.nome} vida {d.vida} ')
if d.is_vivo():
    print('SEU SUBMARINO FOI ABATIDO...GAME OVER!!!')#Se ganhar continua na nova fase
else:
	print('VOCÊ ABATEU O SUBMARINO INIMIGO...AGORA LUTE COM O PROXIMO!!!')
	class SubmarinoB():
		def __init__(self,nome):
			self.nome = nome
			self.vida = 50 #vida do inimigo

		def ataque(self):
			if d100() >= 50: #chance do inimigo te acertar
				return d8() #Maximo de dano que o inimigo pode te causar
			return False

		def dano(self,dano):
			self.vida = self.vida - dano

		def is_vivo(self):
			if self.vida < 1:
				return False
			return True


	#Motor de batalha

	edu = SubmarinoA('URSS')
	d = SubmarinoB('Japan')



	msg = '';
	while edu.is_vivo() and d.is_vivo():

		poder = {
			'1': edu.torpedo04(),
			'2': edu.torpedo08(),
			'3': edu.torpedo012(),
			'4': True
		}

		# print(poder)
		os.system('cls')
		print('\n=========================================')
		print(' 1 Torpedo pequeno-04 (95%)\n',
		'2 Torpedo medio-08 (85%)\n',
		'3 Torpedo grande-012 (75%)')
		print('=========================================')
		print(f'{edu.nome} vida {edu.vida} | {d.nome} vida {d.vida} ')
		print('=========================================')
		print(msg)
		msg = ''
		q = input('Escolha um comando de 1 a 3\n')
		try:
			p = poder[q]
		except:
			p = False
		if p != False:
			if q != '4' and q != '5':
				d.dano(p)
				msg = msg + f'Causo {p} no {d.nome}\n'
			elif q == '5':
				msg = msg + 'Fico Invisivel\n'
			else:
				if edu.autocura():
					msg = msg + 'fez um reparo de emergência\n'
		else:
			msg = msg + 'Ação sem sucesso\n'

		if d.is_vivo():
			d_dano = d.ataque()
			if d_dano != False and p != 'inv':
				msg = msg + f'Você recebeu {d_dano}\n'
				edu.dano(d_dano)
			else:
				msg = msg + 'Submarino inimigo te errou\n'

	print(f'{edu.nome} vida {edu.vida} | {d.nome} vida {d.vida} ')
	if d.is_vivo():
		print('SEU SUBMARINO FOI ABATIDO...GAME OVER!!!')
	else:
		print('VOCÊ ABATEU O SUBMARINO INIMIGO!!!')
