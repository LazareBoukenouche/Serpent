#/usr/bin/python3
#coding:utf-8

#Importe pygame et ses dépendances, et les fichiers du jeu
import pygame
from constantes_jeu import *
from Joueur import Joueur
from pygame.locals import *

#Initialisation et création de la fenetre de jeu.
pygame.init()
pygame.time.set_timer(USEREVENT+1, 100)
ecran = pygame.display.set_mode([600,600])

# Charge les image de fond et du serpent
fond_noir = pygame.image.load('fond.png').convert()
carreRouge = pygame.image.load('carreRouge.png').convert()

# Condition de continuation de la boucle de jeu
continuer = True

serpent = Joueur(height,width,speed,direction,coords_x,coords_y)

# Boucle de jeu principale
while continuer:
	# Rafraichit l'ecran pour afficher le fond noir et l'image du serpent
	# a chaque frame
	
	# Boucle des evenements
	for event in pygame.event.get():

		# Verifie si une touche du clavier est pressee
		cle = pygame.key.get_pressed()

		# Change de direction si une fleche directionnelle est pressee
		if cle[pygame.K_LEFT]:
			serpent.moveLeft()
		if cle[pygame.K_RIGHT]:
			serpent.moveRight()
		if cle[pygame.K_UP]:
			serpent.moveUp()
		if cle[pygame.K_DOWN]:
			serpent.moveDown()
		

		# Termine le jeu si l'on appuie sur la touche Echap
		# ou si le carre depasse les limites de la fenetre
		if cle[pygame.K_ESCAPE] or position[0] < 0 or position[0] \
		> taille_fenetre[0] or position[1] < 0 or position[1] > taille_fenetre[1]:
			continuer = False
			
	serpent.draw(ecran,carreRouge)
	# Met à jour la fenetre pour pouvoir afficher les changements
	pygame.display.flip()
