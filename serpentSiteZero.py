from pygame.locals import *
from random import randint
from constantes_jeu import *
from Menu import *
import pygame
import time
from GameOver import GameOver

class Apple:
    x = 300
    y = 300
    step = 10
 
    def __init__(self,x,y):
        self.x = x * self.step
        self.y = y * self.step
 
    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y)) 
 
 
class Player:
    x = [0]
    y = [0]
    step = 44
    direction = 0
    length = 3
    updateCountMax = 2
    updateCount = 0
 
    def __init__(self, length):
       self.length = length
       for i in range(0,2000):
           self.x.append(-100)
           self.y.append(-100)
 
       # initial positions, no collision.
       self.x[1] = 3*44
       self.x[2] = 3*44
 
    def update(self):
 
        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:
 
            # update previous positions
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
 
            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step
            self.updateCount = 0
 
 
    def moveRight(self):
        if self.direction == 1:
            pass
        else:
            self.direction = 0
 
    def moveLeft(self):
        if self.direction == 0:
            pass
        else:
            self.direction = 1
 
    def moveUp(self):
        if self.direction == 3:
            pass
        else:
            self.direction = 2
 
    def moveDown(self):
        if self.direction == 2:
            pass
        else:
            self.direction = 3 
 
    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i])) 
 
class Game:
    def isCollision(self,x1,y1,x2,y2,bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False
 
class App:
 
    windowWidth = 800
    windowHeight = 600
    player = 0
    apple = 0
    pause = False
    compteur = 0
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._apple_surf = None
        self.game = Game()
        self.player = Player(3) 
        self.apple = Apple(5,5)
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight),pygame.FULLSCREEN)
 
        pygame.display.set_caption('Clone du jeu Snake')
        self._running = True
        self._image_surf = pygame.image.load("ressources/carreRouge.png").convert()
        self._apple_surf = pygame.image.load("ressources/pomme.png").convert()
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        self.player.update()
        pygame.mixer.init()
        son = pygame.mixer.Sound("ressources/son2.wav")
 
        # does snake eat apple?
        for i in range(0,self.player.length):
            if self.game.isCollision(self.apple.x,self.apple.y,self.player.x[i], self.player.y[i],44):
                son.play()
                self.compteur = self.compteur + 1
                self.apple.x = randint(2,9) * 44
                self.apple.y = randint(2,9) * 44
                self.player.length = self.player.length + 1
                score = pygame.font.SysFont('Arial',15,15).render("score:" + str(self.compteur), True, (255, 255, 255))
 
 
        # does snake collide with itself?
        for i in range(2,self.player.length):
            if self.game.isCollision(self.player.x[0],self.player.y[0],self.player.x[i], self.player.y[i],40):
                print("You lose! Collision: ")
                print("x[0] (" + str(self.player.x[0]) + "," + str(self.player.y[0]) + ")")
                print("x[" + str(i) + "] (" + str(self.player.x[i]) + "," + str(self.player.y[i]) + ")")
                continuer = False
                game_over = GameOver([800,600])
 
        pass
        
        # Check if the snake collide with the walls
        if self.player.x[0] < 0 or self.player.y[0] < 0 or self.player.x[0] > self.windowWidth - 8 or self.player.y[0] > self.windowHeight:
            game_over = GameOver([800,600])
            
 
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.player.draw(self._display_surf, self._image_surf)
        self.apple.draw(self._display_surf, self._apple_surf)
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.font.get_fonts()
            arial_fonts = pygame.font.match_font('Arial')
            instructions_quitter = pygame.font.SysFont('Arial',15,15).render("Quitter: [Echap] ", True, (255, 255, 255))
            lancer = pygame.font.SysFont('Arial',15,15).render("Demarrer: [ESPACE] ou [ENTREE] ", True, (255, 255, 255))
            score = pygame.font.SysFont('Arial',15,15).render("score:"+ str(self.compteur), True, (255, 255, 255))
            demarrer = pygame.font.SysFont('Arial',15,15).render("Demarrer", True, (255, 255, 255))
            difficulte = pygame.font.SysFont('Arial',15,15).render("Difficulté: Normale", True, (204, 204,204, 255))
            self._display_surf.blit(instructions_quitter,(350 - instructions_quitter.get_width() // 3, 20 - instructions_quitter.get_height() // 3))
            self._display_surf.blit(lancer,(100 - lancer.get_width() // 3, 20 - lancer.get_height() // 3))
            self._display_surf.blit(score,(500 - score.get_width() // 3, 20 - score.get_height() // 3))
            pygame.draw.rect(self._display_surf,[0,255,255],((0,0),(790,580)),1)
            pygame.display.flip()
            #pygame.event.pump()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.player.moveRight()
         
                    if event.key == K_LEFT:
                        self.player.moveLeft()
         
                    if event.key == K_UP:
                        self.player.moveUp()
         
                    if event.key == K_DOWN:
                        self.player.moveDown()
         
                    if event.key == K_ESCAPE:
                        self._running = False
                        
                    if event.key == K_p:
                        events = pygame.event.wait()
                        if event.key == K_p:
                            break
                
                
            self.on_loop()
            self.on_render()
 
            time.sleep (100.0 / 1000.0);
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
