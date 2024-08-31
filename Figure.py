#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 18:26:49 2023

@author: cr
"""
import pygame,sys
import numpy as np
import Skins

class Figure(pygame.sprite.Sprite):
    
    def __init__(self, name,skins):
         super().__init__()
         self.skins=skins
         self.skin=1
         self.image=skins.get("aktiv_1")
         self.aktiv=True
         self.rect=self.image.get_rect()
         self.angle=0
         self.speed=0
         self.velocity=np.array([0,0])
         self.position=(0,0)
         self.name=name
         self.energy=50
         self.screenposition=(0,0)
         self.IDnumber=0
         self.count_change_pic=0         
         
    def toggle_skin(self):
        if (self.skin==1): 
            self.skin=2
            self.image=self.skins.get("aktiv_2")    
        elif (self.skin ==2): 
            self.skin=1
            self.image=self.skins.get("aktiv_1")    

    def set_IDnumber(self,ID):
        self.IDnumber=ID
        
    def get_IDnumber(self):
        return self.IDnumber

    def update_screen_position(self):
        self.rect.topleft = (self.position[0] * self.skins.field_size[0], self.position[1] * self.skins.field_size[1])

    
    def set_position(self,position):
        self.position=position

    def get_position(self):
        return self.position    

    def get_energy(self):
        return self.energy
    
    def set_screenposition_(self,position=(0,0)):
        self.screenposition=position
        self.rect.topleft =self.screenposition
        
    def get_name(self):
        return self.name
    
    def get_size(self):
        return(self.skins.get_size())

#    def set_move(self, s, omega):
        #rotate1=np.array([[np.cos(self.angle),-1*np.sin(self.angle)],[np.sin(self.angle),np.cos(self.angle)]])
#        self.angle=self.angle+omega
#        if (self.angle>=2*np.pi):self.angle=self.angle-2*np.pi
#        omega=self.angle
#        rotate2=np.array([[+1*np.cos(omega),-1*np.sin(omega)],[+1*np.sin(omega),+1*np.cos(omega)]])
#        self.velocity=rotate2.dot((s,0))
#        print (self.angle)
#        self.image=pygame.transform.rotate(self.pic1,np.degrees(-1*self.angle)) 
        
  
        
    def update(self):
        #screen_x=self.pos_x*self.field_width
        #screen_y=self.pos_y*self.field_height + 50 
        #self.toggle_skin()
        #self.position=self.position+(self.velocity).round(0)
        
        self.count_change_pic+=1
        if self.count_change_pic>=20 :   
            self.toggle_skin()
            self.count_change_pic=0 
           # print("update")
                