#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 15:10:39 2023

@author: cr
"""
import pygame


class Skins():
    def __init__(self, size=1,field_size=(45,45)):
        self.size=size
        self.field_size=field_size
        self.pairs ={}
        
    def add(self,keyword,pic):
        pic_scaled=pygame.transform.scale(pic,(self.size*self.field_size[0],self.size*self.field_size[1])) 
        self.pairs[keyword]=pic_scaled
        
    def get(self,keyword):
        return self.pairs[keyword]
    
    def get_size(self):
        return self.size
    