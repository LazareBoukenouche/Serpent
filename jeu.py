#/usr/bin/python3
#coding:utf-8

#Importe pygame et ses dépendances, et les fichiers du jeu
import pygame
from pygame.locals import *
from constantes_jeu import *

#Initialisation et création de la fenetre de jeu.
pygame.init()
pygame.time.set_timer(USEREVENT+1, 100)
ecran = pygame.display.set_mode(taille_fenetre)

# Charge les image de fond et du serpent
fond_noir = pygame.image.load('fond.png').convert()
carreRouge = pygame.image.load('carreRouge.png').convert()
pomme = pygame.image.load('pomme.jpeg').convert()

# Condition de continuation de la boucle de jeu
continuer = True

#fonctions de deplacement
def bouger(direction):
	position[direction[0]]+= direction[1]

# Boucle de jeu principale
while continuer:
	# Rafraichit l'ecran pour afficher le fond noir et l'image du serpent
	# a chaque frame
	ecran.blit(fond_noir,(0,0))
	ecran.blit(carreRouge,(position))
	# Fait bouger le carre, selon le sens et la vitesse definie dans le
	# fichier constantes_jeu, de base vers la gauche
	bouger(sens_debut)
	# Boucle des evenements
	for event in pygame.event.get():

		# Verifie si une touche du clavier est pressee
		cle = pygame.key.get_pressed()

		# Change de direction si une fleche directionnelle est pressee
		if cle[pygame.K_LEFT]:
			sens_debut = vers_la_gauche
		if cle[pygame.K_RIGHT]:
			sens_debut = vers_la_droite
		if cle[pygame.K_UP]:
			sens_debut = vers_le_haut
		if cle[pygame.K_DOWN]:
			sens_debut = vers_le_bas
			
		# Gere collisions serpent et pomme
		

		# Termine le jeu si l'on appuie sur la touche Echap
		# ou si le carre depasse les limites de la fenetre
		if cle[pygame.K_ESCAPE] or position[0] < 0 or position[0] \
		> taille_fenetre[0] or position[1] < 0 or position[1] > taille_fenetre[1]:
			continuer = False

	# Met à jour la fenetre pour pouvoir afficher les changements
	pygame.display.flip()
