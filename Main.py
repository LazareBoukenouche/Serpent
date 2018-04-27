#/usr/bin/python3
#coding:utf-8

import pygame
from Joueur import Joueur
from pygame.locals import *
        
class Game():
    
    def __init__(self, size_window):

        #Initialisation et création de la fenetre de jeu.
        pygame.init()
        pygame.time.set_timer(USEREVENT+1, 100)
        ecran = pygame.display.set_mode(size_window)
        
        #Initialise les polices textuelles
        pygame.font.init()
        pygame.font.get_fonts()
        arial_fonts = pygame.font.match_font('Arial')
        demarrer = pygame.font.SysFont('Arial',50,50).render("Demarrer", True, (255, 255, 255))
        quitter = pygame.font.SysFont('Arial',50,50).render("Quitter", True, (204, 204,204, 255))


        # Condition de continuation de la boucle de jeu
        continuer = True

        # Boucle de jeu principale
        while continuer:
            # Boucle des evenements
            for event in pygame.event.get():
                # Verifie si une touche du clavier est pressee
                if event.type == MOUSEBUTTONDOWN:
                    if ecran.get_at((pygame.mouse.get_pos())) == (255,255,255,255):
                        print("Lancement du jeu !")
                    elif ecran.get_at((pygame.mouse.get_pos())) == (204,204,204,255):
                        continuer = False
                cle = pygame.key.get_pressed()
            ecran.fill((0,0,0))
            pygame.draw.rect(ecran,[255,255,255],((0,0),(790,590)),1)
            ecran.blit(demarrer,(320 - demarrer.get_width() // 2, 240 - demarrer.get_height() // 2))
            ecran.blit(quitter,(320 - quitter.get_width() // 2, 340 - quitter.get_height() // 2))      
            # Met à jour la fenetre pour pouvoir afficher les changements
            pygame.display.flip()
            
main = Game([800,600])
