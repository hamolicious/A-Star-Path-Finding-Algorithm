import pygame

class Node:
    def __init__(self, x, y, mode):
        self.x = x
        self.y = y

        self.pos = pygame.math.Vector2(self.x, self.y)

        self.mode = mode

    def show(self, screen):
        if self.mode == 0:
            pygame.draw.circle(screen, [0, 200, 200], (self.x + 10, self.y + 10), 10)
        if self.mode == 1:
            pygame.draw.circle(screen, [200, 200, 0], (self.x + 10, self.y + 10), 10)

    def update(self, mousePos, mousePressed, grid):
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        self.pos = pygame.math.Vector2(self.x, self.y)

        if self.rect.collidepoint(mousePos) and mousePressed == (1, 0, 0):
            self.x, self.y = mousePos[0] - 10, mousePos[1] - 10
            return True
        else:
            index = self.rect.collidelist(grid)
            self.x = grid[index][0]
            self.y = grid[index][1]
            return False
