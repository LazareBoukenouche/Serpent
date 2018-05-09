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
            surface.blit(image,(self.coords_x[i],self.coords_y[i]))
            
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
       self.x[1] = 2*44
       self.x[2] = 2*44
 
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
        self.direction = 0
 
    def moveLeft(self):
        self.direction = 1
 
    def moveUp(self):
        self.direction = 2
 
    def moveDown(self):
        self.direction = 3 
 
    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i])) 
