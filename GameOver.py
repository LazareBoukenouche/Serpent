#/usr/bin/python3
#coding:utf-8

from serpentSiteZero import *

BLACK = (0,0,0)

class GameOver():
    
    def __init__(self, size_window):

        #Initialisation et création de la fenetre de jeu.
        pygame.init()
        pygame.time.set_timer(USEREVENT+1, 100)
        ecran = pygame.display.set_mode(size_window, pygame.FULLSCREEN)
        
        #Initialise les polices textuelles
        pygame.font.init()
        pygame.font.get_fonts()
        arial_fonts = pygame.font.match_font('Arial')
        instructions_quitter = pygame.font.SysFont('Arial',20,20).render("Quitter la partie : Echap ", True, (255, 255, 255))
        reset = pygame.font.SysFont('Arial',50,50).render("Rejouer ?", True, (255, 255, 255))
        difficulte = pygame.font.SysFont('Arial',50,50).render("Difficulté: Normale", True, (204, 204,204, 255))


        # Condition de continuation de la boucle de jeu
        continuer = True

        # Boucle de jeu principale
        while continuer:
            # Boucle des evenements
            for event in pygame.event.get():
                # Verifie si une touche du clavier est pressee
                
                # Si la souris survole le texte, celui-ci devient bleu et l'autre reste blanc
                if event.type == MOUSEMOTION and ecran.get_at((pygame.mouse.get_pos())) == (255,255,255,255):
                    reset = pygame.font.SysFont('Arial',50,50).render("Rejouer ?", True, (0, 100,255, 255))
                elif event.type == MOUSEMOTION and ecran.get_at((pygame.mouse.get_pos())) == (204,204,204,255):
                    reset = pygame.font.SysFont('Arial',50,50).render("Rejouer ?", True, (255, 255,255, 255))
                
                # Verifie si la souris est pressee
                if event.type == MOUSEBUTTONDOWN:
                    # Si on clique sur Demarrer, on lance le jeu
                    if ecran.get_at((pygame.mouse.get_pos())) == (0,100,255,255):
                        print("On Recommence le jeu !")
                        reset = pygame.font.SysFont('Arial',50,50).render("Rejouer ?", True, (0, 0,255, 255))
                        ecran.fill(BLACK)
                        theApp = App()
                        theApp.on_execute()
                        
                    
                # Verifie les evenments du clavier
                if event.type == KEYDOWN:
                    # Si on appuie sur Echap, quitter le jeu
                    if event.key == K_ESCAPE:
                        continuer = False
                    if event.key == K_1:
                        difficulte = pygame.font.SysFont('Arial',50,50).render("Difficulté: Easy", True, (204, 204,204, 255))
                    if event.key == K_LEFT:
                        difficulte = pygame.font.SysFont('Arial',50,50).render("Difficulté: Hard", True, (204, 204,204, 255))
                    if event.key == K_RETURN:
                        theApp = App()
                        theApp.on_execute()
                        
            ecran.fill(BLACK)
            pygame.draw.rect(ecran,[255,255,255],((0,0),(790,590)),1)
            ecran.blit(instructions_quitter,(100 - instructions_quitter.get_width() // 3, 20 - instructions_quitter.get_height() // 3))
            ecran.blit(reset,(355 - reset.get_width() // 2, 240 - reset.get_height() // 2))
            ecran.blit(difficulte,(450 - difficulte.get_width() // 2, 340 - difficulte.get_height() // 2)) 
            # Met à jour la fenetre pour pouvoir afficher les changements
            pygame.display.flip()
            

