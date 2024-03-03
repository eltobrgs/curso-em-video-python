#Tocando um MP3
import pygame
pygame.init()
pygame.mixer.music.load('desafios de python/castelvania.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()