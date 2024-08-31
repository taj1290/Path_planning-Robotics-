#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 08:23:05 2023

@author: cr
"""
import Figure
import Aobject


class Animation_queue():

    def __init__(self,frames_per_picture=10,steps=3):
        self.frames_per_picture=frames_per_picture
        self.steps=steps
        self.move_list = []
        self.count=0

    def add_fig(self,figure,screen_pos_i,screen_pos_f):
        self.move_list.append(Aobject.animation_object(figure,screen_pos_i,screen_pos_f,self.steps))        
        
    def animate(self):
        self.count+=1
        if self.count>=self.frames_per_picture :
            for i in self.move_list :
                if i.move() :
                    self.move_list.remove(i)
            self.count=0
        
    def isin_animation(self, figure):
        for i in self.move_list :
            if i.figure==figure : return True
        return False
        