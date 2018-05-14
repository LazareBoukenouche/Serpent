#/usr/bin/python3
#coding:utf-8

#Importe pygame et ses dépendances, et les fichiers du jeu
import pygame
from pygame.locals import *
from random import randint
from constantes_jeu import *

#Initialisation et création de la fenetre de jeu.
pygame.init()
ecran = pygame.display.set_mode(taille_fenetre, pygame.FULLSCREEN)


# Condition de continuation de la boucle de jeu
continuer = True

# Boucle de jeu principale
while continuer:
	
	# Boucle des evenements
	for event in pygame.event.get():
		
		if event.type == KEYDOWN:
			# Change de direction si une fleche directionnelle est pressee
			if event.key == pygame.K_LEFT:
				serpent.moveLeft()
			if event.key == pygame.K_RIGHT:
				serpent.moveRight()
			if event.key == pygame.K_UP:
				serpent.moveUp()
			if event.key == pygame.K_DOWN:
				serpent.moveDown()
				
			if event.key == pygame.K_RETURN:
				print("test")
				game_over = GameOver([800,600])
				
			#Termine le jeu si l'on appuie sur Echap ou si l'on touche les murs	
			if event.key == pygame.K_ESCAPE or position[0] < 0 or position[0] \
		> taille_fenetre[0] or position[1] < 0 or position[1] > taille_fenetre[1]:
				continuer = False
				
	pygame.display.flip()
