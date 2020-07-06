# -*- coding: utf-8 -*-
#Figth Engine - Monster Duel
#@author: Eduardo Q Marques 02-07-2020
from random import randint
import os
import time
import winsound
#import sys

def d100():
    return randint(1,100)

#Attack
def dog(bite, hand, esc):
    bite = randint(1,50)
    hand = randint(1,20)
    esc = randint(1,20)

def cat(bite, hand, esc):
    bite = randint(1,25)
    hand = randint(1,40)
    esc = randint(1,80)

def rat(bite, hand, esc):
    bite = randint(1,15)
    hand = randint(1,10)
    esc = randint(1,50)