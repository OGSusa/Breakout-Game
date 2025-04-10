import pygame
WHITE = (255, 255, 255)
PADDLE_WIDTH, PADDLE_HEIGHT, = 100, 20

class Paddle:
    COLOR = WHITE
    VEL = 8

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, left=True):
        if left:
            self.x -= self.VEL
        else:
            self.x += self.VEL
