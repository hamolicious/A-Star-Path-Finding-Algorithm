import pygame

class Button:
    def __init__(self, colour, colourHover, x, y, w, h, font, text):
        self.colour = colour
        self.colourHover = colourHover
        self.colourMain = colour
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.font = font
        self.text = text

    def show(self, screen):
        pygame.draw.rect(screen, self.colourMain, (self.x, self.y, self.w, self.h), 0)
        screen.blit(self.font.render(self.text, 1, [0, 0, 0]), (self.x, self.y))

    def onPressed(self, mouse_pos, mouse_pressed):
        if mouse_pressed == (1, 0, 0):
            return pygame.Rect(self.x, self.y, self.w, self.h).collidepoint(mouse_pos)

    def onHover(self, mouse_pos):
        if pygame.Rect(self.x, self.y, self.w, self.h).collidepoint(mouse_pos) == True:
            self.colourMain = self.colourHover
        else:
            self.colourMain = self.colour

