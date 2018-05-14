#/usr/bin/python3
#coding:utf-8

import pygame
from pygame.locals import *
BLACK = (0,0,0)

class Regles():
    
    def __init__(self, size_window):

        #Initialisation et création de la fenetre de jeu.
        pygame.init()
        pygame.time.set_timer(USEREVENT+1, 100)
        pygame.display.set_caption(" Clone du jeu Snake")
        ecran = pygame.display.set_mode(size_window, pygame.FULLSCREEN)
        
        #Initialise les polices textuelles
        pygame.font.init()
        pygame.font.get_fonts()
        arial_fonts = pygame.font.match_font('Arial')
        regles1 = pygame.font.SysFont('Arial',20,20).render("Les règles du jeu :", True, (255, 255, 255))
        regles2 = pygame.font.SysFont('Arial',20,20).render("Le joueur contrôle un serpent qui doit manger une pomme,", True, (255, 255, 255))
        regles3 = pygame.font.SysFont('Arial',20,20).render("pour faire grandir le serpent.",True, (255, 255, 255))
        regles4 = pygame.font.SysFont('Arial',20,20).render("Le serpent avance sans arret et le joueur indique une direction:",True, (255, 255, 255)) 
        regles5 = pygame.font.SysFont('Arial',20,20).render(" ←,↓,→,↑.", True, (255, 255, 255))
        regles6 = pygame.font.SysFont('Arial',20,20).render("Si la tête du serpent touche les murs,", True, (255, 255, 255))
        regles7 = pygame.font.SysFont('Arial',20,20).render("ou son propre corps, la partie est finie.", True, (255, 255, 255))
        retour = pygame.font.SysFont('Arial',20,20).render("Pour retourner à l'ecran de demarrage, appuyer sur [Echap]", True, (255, 255, 255))
        # Condition de continuation de la boucle de jeu
        continuer = True

        # Boucle de jeu principale
        while continuer:
            # Boucle des evenements
            for event in pygame.event.get():
                        
                # Verifie les evenments du clavier
                if event.type == KEYDOWN:
                    # Si on appuie sur Echap, quitter le jeu
                    if event.key == pygame.K_ESCAPE:
                        continuer = False
                    
            ecran.fill(BLACK)
            pygame.draw.rect(ecran,[0,255,255],((0,0),(790,590)),1)
            
            #Afficher les textes
            ecran.blit(regles1,(100 - regles1.get_width() // 3, 20 - regles1.get_height() // 3))
            ecran.blit(regles2,(300 - regles2.get_width() // 3, 80 - regles2.get_height() // 3))
            ecran.blit(regles3,(195 - regles3.get_width() // 3, 140 - regles3.get_height() // 3))
            ecran.blit(regles4,(320 - regles4.get_width() // 3, 200 - regles4.get_height() // 3))
            ecran.blit(regles5,(120 - regles5.get_width() // 3, 240 - regles5.get_height() // 3))
            ecran.blit(regles6,(225 - regles6.get_width() // 3, 300 - regles6.get_height() // 3))
            ecran.blit(regles7,(225 - regles7.get_width() // 3, 360 - regles7.get_height() // 3))
            
            
            ecran.blit(retour,(250 - retour.get_width() // 3, 500- retour.get_height() // 3))
                  
            # Met à jour la fenetre pour pouvoir afficher les changements
            pygame.display.flip()


