import pygame

WIDTH, HEIGHT = 1200, 800


class Scoreboard:
    def __init__(self, score=0, lives=3):
        self.score = score
        self.lives = lives
        self.font = pygame.font.Font(None, 40)

    def add_points(self, amount):
        self.score += amount

    def lose_life(self, amount=1):
        self.lives -= amount

    def draw(self, win):
        points = f'Score: {self.score}'
        lives = f'Lives: {self.lives}'
        points_text = self.font.render(points, True, (255, 255, 255))
        lives_text = self.font.render(lives, True, (255, 255, 255))
        win.blit(points_text, (10, 10))
        win.blit(lives_text, (WIDTH - 120, 10))
