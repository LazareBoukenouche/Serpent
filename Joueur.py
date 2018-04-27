#/usr/bin/python3
#coding:utf-8

#Importe pygame et ses dépendances, et les fichiers du jeu
import pygame
from pygame.locals import *

class Joueur():
    def __init__(self,height,width,speed,direction,coords_x,coords_y):
        self.height = height
        self.width = width
        self.speed = speed
        self.direction = direction
        self.coords_x = coords_x
        self.coords_y = coords_y
        self.length = 1
        
    def start_moving(self,):
        self.height = self.height + self.speed
 
    def moveLeft(self):
        self.height = self.height + self.speed
    
    def moveRight(self):
        self.height = self.height + self.speed
 
    def moveUp(self):
        self.width = self.width - self.speed
 
    def moveDown(self):
        self.width = self.width + self.speed

        
    def grow(self,width):
        self.width = width
        pass
    
    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i]))

