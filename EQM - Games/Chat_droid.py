# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Test')

convI = ['oi', 'olá', 'olá, bom dia',
'bom dia, como vai?', 'estou bem!']

convF = ['Que filmes vc gosta?',
'Eu gosto de JurrasicPark!']

bot.set_trainer(ListTrainer)

bot.train(convI)
bot.train(convF)

while True:
		quest = input('Você: ')
		
		response = bot.get_response
(quest)

print('Bot: ', response)
