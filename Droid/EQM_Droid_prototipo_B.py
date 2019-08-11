#EQM Droid (prototipo)
#Teste1
#Colaboração: Jairo Matos da Rocha
#16/04/2018
from tkinter import *
import time
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Droid - 2")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Enviar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
        self.txt = 'Olá!'
        self.mensagem['text'] = self.txt
        self.tempo = 0
        self.mensagem.after(5000, self.eduprint, 'Qual é o seu nome?')

    def time(self,t):
        self.tempo = self.tempo+(t*1000)
        return self.tempo

    def verificaSenha(self):
        myName = self.nome.get()
        self.mensagem.after(self.time(3), self.eduprint,'É um prazer conhece-lo, ' + myName)
        #time.sleep(3)#pause in seconds before other frases
        self.mensagem.after(self.time(3), self.eduprint,'Eu sou o segundo prototipo de robô da E.Q.M-CORPORATION...')
        #time.sleep(3)
        self.mensagem.after(self.time(3), self.eduprint,'Meu criador é o Eduardo Q Marques...')
        #time.sleep(3)
        self.mensagem.after(self.time(3), self.eduprint,'Ele gosta muito de mim e acredita no meu potêncial!')
        #time.sleep(3)
        self.mensagem.after(self.time(3), self.eduprint,'Em breve serei mais inteligente e autônomo!')
        #time.sleep(3)
        self.mensagem.after(self.time(3), self.eduprint,'Mas agora tenho que me desligar!')
        #time.sleep(3)
        self.mensagem.after(self.time(3), self.eduprint,'Até mais, ' + myName)
        #time.sleep(3)
        self.mensagem.after(self.time(5), self.eduprint,'ENCERRANDO Droid-1')
        #time.sleep(5)

    def eduprint(self,smg):
        self.txt = self.txt +'\n'+ smg
        self.mensagem["text"] = self.txt

root = Tk()
app = Application(master = root)
app.master.title('EQM - CORPORATION')
root.mainloop()
