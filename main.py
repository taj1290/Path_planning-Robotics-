#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 16:12:39 2023

@author: cr
"""

import pygame
import numpy as np
import Figure
import World
import Scorescreen
import Skins
from collections import deque
import heapq  # For priority queue in A* algorithm

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
field_size = (30, 30)
figure_size = 1
figure_sight = 2
theWorld = World.World((30, 30), field_size, file_name="maze1.maz")
print("Created World:", theWorld.get_screensize())
scorescreen = Scorescreen.Scorescreen((theWorld.get_screensize()[0], 0), (250, theWorld.get_screensize()[1]), "white", True)

screen = pygame.display.set_mode((theWorld.get_screensize()[0] + scorescreen.get_screensize()[0], theWorld.get_screensize()[1]))
pygame.display.set_caption("Clean.....")

skins = Skins.Skins(figure_size, field_size)
figure_hold = pygame.image.load("./graphics/cleaner1.png")
figure_move = pygame.image.load("./graphics/cleaner2.png")
scorescreen.set_symbol(figure_hold)
skins.add("aktiv_1", figure_hold)
skins.add("aktiv_2", figure_move)

fig = Figure.Figure("Cleaner 1", skins)
theWorld.add_figure(fig)

current_fig = fig
view = theWorld.get_view(current_fig, figure_sight)
print(view)


def draw_screen(rounds=1):
    i = 0
    view = theWorld.get_view(current_fig, figure_sight)
    while i <= rounds:
        screen.fill((0, 0, 0))  # Clear the screen before drawing
        theWorld.draw(screen)
        theWorld.animate_movements()
        scorescreen.draw(screen, moves, current_fig, view)
        fig_group.draw(screen)
        pygame.display.flip()
        clock.tick(30)
        i += 1


def heuristic(a, b):
    # Using Euclidean distance as heuristic
    return np.linalg.norm(np.array(a) - np.array(b))


def hybrid_a_star(start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))  # Priority queue with (cost, position)
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if (0 <= neighbor[0] < theWorld.world_size[0] and
                0 <= neighbor[1] < theWorld.world_size[1] and
                theWorld.map[neighbor[0], neighbor[1]] != 1):
                tentative_g_score = g_score[current] + 1
                if (neighbor not in g_score or tentative_g_score < g_score[neighbor]):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                    if neighbor not in [i[1] for i in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None


spielaktiv = True

fig_group = pygame.sprite.Group()
fig_group.add(fig)
fig_group.draw(screen)
moves = 0

pygame.display.flip()

# Start and goal positions
start = theWorld.starting_pos
goal = theWorld.goal_pos

# Hybrid A* to find the path
path = hybrid_a_star(start, goal)

if path:
    for position in path:
        fig.set_position(position)
        fig.update_screen_position()
        fig.update()  # Update the figure to switch skins
        draw_screen()
else:
    print("No path to goal found.")

pygame.display.quit()
pygame.quit()