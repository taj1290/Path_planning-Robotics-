#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 15:37:37 2023

@author: cr
"""
import pygame
import numpy as np

class Scorescreen():
    def __init__(self,position=(0,0),size=(250,900), background="white",frame_on=True):
        self.size=size
        self.frame_on=frame_on
        self.position=position
        self.background=background
        self.myFont=pygame.font.SysFont('Comic Sans MS',15)        
        
    def get_screensize(self):
        return self.size

    
    def set_symbol(self,figure_symbol):
        self.figure_symbol=figure_symbol 
        
    def draw(self,screen,moves,fig,view):
        color=pygame.Color(self.background)
        rect=(self.position,self.size)
        pygame.draw.rect(screen,color,rect)
        text_surface= self.myFont.render("Amount of rounds: "+str(moves), True, (0,0,0))
        xy=np.array(self.position)+np.array((20,30))
        screen.blit(text_surface,xy)
        screen.blit(self.figure_symbol,(self.position[0]+10,self.position[1]+120))
        text_surface= self.myFont.render(fig.get_name(), True, (0,0,0))    
        screen.blit(text_surface,(self.position[0]+20,self.position[1]+220))
        text_surface= self.myFont.render("Energy: ", True, (0,0,0))
        screen.blit(text_surface,(self.position[0]+20,self.position[1]+270))
        
        color=pygame.Color("cadetblue1")
        rect=(self.position[0]+20,self.position[1]+290,200,30)
        pygame.draw.rect(screen,color,rect,width=0)
        
        color=pygame.Color("cadetblue")
        rect=(self.position[0]+20,self.position[1]+290,int(2*fig.get_energy()),30)
        pygame.draw.rect(screen,color,rect,width=0)
        
        rect=(self.position[0]+20,self.position[1]+290,200,30)
        color=pygame.Color("black")
        pygame.draw.rect(screen,color,rect,width=3)
        
        text_surface= self.myFont.render("View: ", True, (0,0,0))
        screen.blit(text_surface,(self.position[0]+20,self.position[1]+400))
        
        
        wall_color=pygame.Color("darkolivegreen4")
        free_color=pygame.Color("white")
        size=int(200/view[0].size)
        for y in range(0,view[1].size):    
            for x in range(0,view[0].size):
                #print (view)
                #print(x,",",y)
                #print(view[x][y])
                if (view[x][y]==0): 
                    pygame.draw.rect(screen,free_color,(self.position[0]+20+x*size,self.position[1]+420+y*size,size,size))                

                if (view[x][y]==1): 
                    pygame.draw.rect(screen,wall_color,(self.position[0]+20+x*size,self.position[1]+420+y*size,size,size))                
        color=pygame.Color("black")
        rect=(self.position[0]+20,self.position[1]+420,size*view[0].size,size*view[0].size)
        pygame.draw.rect(screen,color,rect,width=3)

        if self.frame_on: 
            color=pygame.Color("black")
            rect=(self.position,self.size)
            pygame.draw.rect(screen,color,rect,width=5)
            
        