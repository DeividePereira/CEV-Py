#import playsound
#playsound.playsound('desafio.mp3')
#Não funcionou.
#Muitos códigos de reprodução de áudio não funcionam.
#A função input faz a maioria deles funcionar.

import pygame
pygame.init()
pygame.mixer.music.load('desafio021.mp3')
input('Digite algo para tocar: ')
pygame.mixer.music.play()
print('Ooohhhh YYYEEEeesss!')
input('Digite algo para parar: ')
