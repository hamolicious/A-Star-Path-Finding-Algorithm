import pygame
from math import sqrt

def dist(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

class Node:
    def __init__(self, x, y, mode, start_node, end_node):
        self.x = x
        self.y = y

        self.g = int(dist(self.x, self.y, start_node.x, start_node.y))
        self.h = int(dist(self.x, self.y, end_node.x, end_node.y))
        self.f = self.g + self.h

        # wall or node
        self.mode = mode

        self.parent = None

        self.size = 0
        self.sizeMax = 10

    def show(self, screen):
        if self.mode == 'wall':
            pygame.draw.rect(screen, [100, 100, 100], (self.x, self.y, 20, 20), 0)
        if self.mode == 'hidden':
            pygame.draw.rect(screen, [51, 51, 51], (self.x, self.y, 20, 20), 1)
        if self.mode == 'open':
            pygame.draw.circle(screen, [0, 200, 0], (self.x + 10, self.y + 10), self.size)
        if self.mode == 'closed':
            pygame.draw.circle(screen, [200, 0, 0], (self.x + 10, self.y + 10), self.size)

        if self.mode != 'hidden' and self.mode != 'wall':
            if self.size < self.sizeMax:
                self.size += 2

    def update(self, mousePos):
        self.rect = pygame.Rect(self.x, self.y, 20, 20)

        if self.rect.collidepoint(mousePos) and self.mode == 'closed':
            pygame.display.set_caption('F cost {} | G cost {} | H cost {}'.format(self.f, self.g, self.h))
