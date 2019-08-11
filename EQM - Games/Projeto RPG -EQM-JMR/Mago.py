from Dado import d100


class Mago():

    def __init__(self,nome):
        self.nome = nome
        self.vida = 20

    def boladefogo(self):
        if d100() >= 25:
            return 'Sucesso'
        return 'Fudeu'

    def congelar(self):
        if d100() >= 25:
            return 'Sucesso'
        return 'Fudeu'

    def ficarinvisivel(self):
        if d100() >= 50:
            return 'Sucesso'
        return 'Fudeu'

    def autocura(self):
        if d100() >= 95:
            self.vida = 20
            return 'Sucesso'
        return 'Fudeu'

    def invocartiamat(self):
        if d100() >= 90:
            return 'Sucesso'
        return 'Fudeu'

    def dano(self,dano):
        self.vida = self.vida - dano

    def is_vivo(self):
        if self.vida < 1:
            return False
        return True

    def __repr__(self):
        return f'Sou {self.nome} tenho {self.vida} pontos de vida' #Ver as live de python para aprender
