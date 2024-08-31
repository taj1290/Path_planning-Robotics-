#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 09:05:15 2023

@author: cr
"""

class animation_object():
    def __init__(self,figure,screen_pos,screen_pos_f,steps=3):
        self.figure=figure
        self.screen_pos=screen_pos
        self.screen_pos_f=screen_pos_f
        self.steps=steps
        self.delta_x=int((screen_pos_f[0]-screen_pos[0])/steps)
        self.delta_y=int((screen_pos_f[1]-screen_pos[1])/steps)
        #print(self.delta_x)
        #print(self.screen_pos[0])
        self.count=0
        
    def move(self):
        self.count=self.count+1
        if (self.count>=self.steps) :
            self.figure.set_screenposition_(self.screen_pos_f)
            print("reached final position")
            self.count=0
            return True # reached final position
        self.screen_pos=(self.screen_pos[0]+self.delta_x,self.screen_pos[1]+self.delta_y)
        self.figure.set_screenposition_(self.screen_pos)
        #self.figure.set_screenposition(self.screen_pos) 
        return False # not reached final position
