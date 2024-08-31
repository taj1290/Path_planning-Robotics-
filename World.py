#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 10:54:44 2023

@author: cr
"""
import pygame
import numpy as np
import Figure
import Animation
import random



class World():
    
    def __init__(self,world_size=(20,22),field_size=(45,45),file_name=""):
        self.field_size=field_size
        self.starting_pos=(0,0)
        self.goal_pos=(0,0)
        # if file_name=="" : self.world_size=world_size
        self.world_size=world_size
        (self.map,self.dirt)=self.load_world(file_name)
        self.figures=['a']
        # layer of the battle field that hold positions of figures
        # which field is occupied by which figure
        self.positions=np.zeros(world_size,int) 
        self.animation=Animation.Animation_queue(3,5)
        (self.labeled_fields, self.labels_to_field)=self.create_labeled_fields() 
        print(self.labeled_fields)
        
         
    def create_labeled_fields(self):
        liste=list(range(0,self.map.size))
        fields=np.zeros(self.world_size)
        myhash={}
        for y in range(0,self.world_size[1]):    
            for x in range(0,self.world_size[0]):
                number=random.randint(0,len(liste)-1)
                keyword=liste[number]
                fields[x][y]=keyword
                myhash[keyword]=(x,y)
        return (fields,myhash)        

    def get_screensize(self):
        return (self.world_size[0]*(0+self.field_size[0]),self.world_size[1]*(0+self.field_size[1]))        
        

    def load_world(self, filename):
        # 1= wand
        dirt= np.ones((self.world_size[0],self.world_size[1]))
        map1=np.zeros((self.world_size[0],self.world_size[1]))
  
        fobj=open(filename,"r")
        line_count=0
        for line in fobj:
            line_count=line_count+1
            one_line=line.rstrip()      
            lenth=len(one_line)
            c_count=0
            for c in one_line:
                c_count=c_count+1
                if (c_count<=self.world_size[0]):
                    if (c=="x"): 
                        map1[c_count-1,line_count-1]=1
                        dirt[c_count-1,line_count-1]=0
                    if (c=="s"):self.starting_pos=(c_count-1,line_count-1)
                    if (c=="g"):self.goal_pos=(c_count-1,line_count-1)
        return (map1,dirt*100)

    def add_figure(self,figure,position=(-1,-1)):
        self.figures.append(figure)
        x=self.figures.index(figure)
        figure.set_IDnumber(x)
        if (position==(-1,-1)): position=self.starting_pos
        figure.set_position(position)
        #self.positions[position[0]:position[0]+figure.get_size(),position[1]:position[1]+figure.get_size()]=x
        #print(self.positions)
        if (self.place(figure,(0,0))):
            figure.set_screenposition_((position[0]*self.field_size[0],position[1]*self.field_size[1]))
            return True
        figure.set_position((-1,-1))
        
        print("Cannot add figure:",figure.name," with ID:",x," to map, because field is blocked")
            
        
    def place(self,figure,direction=(0,0)):
        position=figure.get_position()
        # Figure layer - would there be a collision
        myID=figure.get_IDnumber()
        positions_old=self.positions[position[0]:position[0]+figure.get_size(),position[1]:position[1]+figure.get_size()]
        positions_m=self.positions[position[0]+direction[0]:position[0]+figure.get_size()+direction[0],position[1]+direction[1]:position[1]+figure.get_size()+direction[1]]
        if(np.count_nonzero((positions_m!=myID) & (positions_m!=0))==0): # Collision with other player
            map_part=self.map[position[0]+direction[0]:position[0]+figure.get_size()+direction[0],position[1]+direction[1]:position[1]+figure.get_size()+direction[1]]    
            if ((position[0]+direction[0]>=0) and (position[1]+direction[1]>=0) and (position[0]+figure.get_size()+direction[0]<=self.world_size[0]) 
                and (position[1]+direction[1]+figure.get_size()<=self.world_size[1])):
                if (np.count_nonzero((map_part!=0) & (map_part!=0))==0):
                    #print("Working on:",myID)
                    #print(position[0]+direction[0],":",position[0]+figure.get_size()+direction[0],",",position[1]+direction[1],":",position[1]+figure.get_size()+direction[1])
                    #print(positions_m)
                    positions_old[:]=0
                    positions_m[:]=myID
                    #print(self.positions)
                    return True
                print ("Cannot place: wall")
                return False
            print ("Cannot place: out of world")
            return False
        print("Cannot place - other player")
        return False            
        
        
    
        
    def move_fig(self,figure,direction):
        if self.animation.isin_animation(figure): return False # no movements if still animated
        if self.place(figure,direction):
           
            new_position=(figure.get_position()[0]+direction[0],figure.get_position()[1]+direction[1])
            self.animation.add_fig(figure,(figure.get_position()[0]*self.field_size[0],figure.get_position()[1]*self.field_size[1]),(new_position[0]*self.field_size[0],new_position[1]*self.field_size[1]))
            figure.set_position(new_position)
            #figure.set_screenposition((new_position[0]*self.field_size[0],new_position[1]*self.field_size[1]))
            return True # could move
        return False # could not move
    
    def animate_movements(self):
        self.animation.animate()
        
                
    def draw(self,screen):
        goal_color=pygame.Color("gold")
        wall_color=pygame.Color("darkolivegreen4")
        dirt_color25=pygame.Color("cornsilk")
        dirt_color50=pygame.Color("cornsilk1")
        dirt_color75=pygame.Color("cornsilk2")
        dirt_color100=pygame.Color("cornsilk3")
   
        for y in range(0,self.world_size[1]):    
            for x in range(0,self.world_size[0]):
                if (self.map[x][y]==1): 
                    pygame.draw.rect(screen,wall_color,(x*self.field_size[0],y*self.field_size[1],self.field_size[0],self.field_size[0]))                
                if (self.dirt[x][y]>0 and self.dirt[x][y]<=25): 
                    pygame.draw.rect(screen,dirt_color25,(x*self.field_size[0],y*self.field_size[1],self.field_size[0],self.field_size[0]))
                if ((self.dirt[x][y]>25) and (self.dirt[x][y]<=50)): 
                    pygame.draw.rect(screen,dirt_color50,(x*self.field_size[0],y*self.field_size[1],self.field_size[0],self.field_size[0]))
                if ((self.dirt[x][y]>50) and (self.dirt[x][y]<=75)): 
                    pygame.draw.rect(screen,dirt_color75,(x*self.field_size[0],y*self.field_size[1],self.field_size[0],self.field_size[0]))
                if ((self.dirt[x][y]>75)): 
                    pygame.draw.rect(screen,dirt_color100,(x*self.field_size[0],y*self.field_size[1],self.field_size[0],self.field_size[0]))
        #Goal 
        x=self.goal_pos[0]
        y=self.goal_pos[1]
        pygame.draw.rect(screen,goal_color,(x*self.field_size[0],y*self.field_size[1],self.field_size[0],self.field_size[0]))
    #def move_fig()      
    
    
    
    def reached_goal(self, figure):
        position=figure.get_position()
        if (position==self.goal_pos): return True
        return False
    
    def move_fig(self, figure, direction):
        if self.animation.isin_animation(figure):
            return False  # no movements if still animated
        if self.place(figure, direction):
            new_position = (figure.get_position()[0] + direction[0], figure.get_position()[1] + direction[1])
            self.animation.add_fig(figure, (figure.get_position()[0] * self.field_size[0], figure.get_position()[1] * self.field_size[1]),
                                (new_position[0] * self.field_size[0], new_position[1] * self.field_size[1]))
            figure.set_position(new_position)
            figure.update_screen_position()  # Update the screen position
            return True  # could move
        return False  # could not move

    
    def get_view(self,figure, sight=3):
        # 0 there is nothing
        # -1 I do not know
        # 1 wall
        # 2 goal
        position=figure.get_position()
        direction=(1,0)
        m=np.array(self.map)
        # if close to the end of the world calculating additional rows and coloums of matrix
        # first building matrix independent from direction in which the figure is looking

        add_left= sight-position[0]
        if add_left >0:
            columns=np.ones((add_left,m.shape[1]),int)
            m=np.vstack([columns,m])  
        if add_left <0: add_left=0;
        
        add_right= sight+position[0]+figure.get_size()-self.world_size[0]+1
        if add_right >0:
            columns=np.ones((add_right,m.shape[1]),int)
            m=np.vstack([m,columns])   
        
        add_top= sight-position[1]
        if add_top > 0:
            rows_above=np.ones((m.shape[0],add_top),int)
            m=np.hstack([rows_above,m])    
        if add_top <0: add_top=0;
        
        add_buttom= sight+position[1]+figure.get_size()-self.world_size[1]+1
        if add_buttom > 0:
            rows_buttom=np.ones((m.shape[0],add_buttom),int)
            m=np.hstack([m,rows_buttom])   
        
    
        position=(position[0]+add_left,position[1]+add_top)
        
        
        mm=m[position[0]-sight:position[0]+sight+figure.get_size(),position[1]-sight:position[1]+figure.get_size()+sight]
        
        return mm
        