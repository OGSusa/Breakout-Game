import pygame
from scoreboard import Scoreboard

WIDTH, HEIGHT = 1200, 800
WHITE = (255, 255, 255)
BALL_RADIUS = 7
PADDLE_WIDTH, PADDLE_HEIGHT, = 100, 20

class Ball:
    MAX_VEL = 8
    COLOR = WHITE

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = 0
        self.y_vel = self.MAX_VEL

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self, paddle, blocks, scoreboard):
        steps = self.MAX_VEL
        for _ in range(steps):
            self.x += self.x_vel / steps
            self.y += self.y_vel / steps
            self.check_collision(paddle, blocks, scoreboard)

    def check_collision(self, paddle, blocks, scoreboard):
        # If ball hits the top of the screen
        if self.y - self.radius <= 0:
            self.y_vel *= -1

        # If ball hits the sides of the screen
        if self.x + self.radius >= WIDTH or self.x - self.radius <= 0:
            self.x_vel *= -1

        # If ball hits the paddle
        if self.y_vel > 0:
            if paddle.x <= self.x <= paddle.x + PADDLE_WIDTH:
                if self.y + self.radius >= paddle.y:
                    self.y_vel *= -1

                    middle_x = paddle.x + paddle.width / 2
                    difference_in_x = middle_x - self.x
                    reduction_factor = (paddle.width / 2) / self.MAX_VEL
                    x_vel = difference_in_x / reduction_factor
                    self.x_vel = -x_vel

        # If ball hits a block
        for block in blocks:
            # Use rectangles to detect collision
            block_rect = pygame.Rect(block.x, block.y, block.BLOCK_WIDTH, block.BLOCK_HEIGHT)
            ball_rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

            # Make sure the ball does not hit 2 blocks in a row
            collided = False

            if not collided and ball_rect.colliderect(block_rect):
                block.gets_hit(blocks)
                scoreboard.add_points(5)
                collided = True
                # Invert ball.y_vel or ball.x_vel depending on where the collision happened
                if block.x <= self.x <= block.x + block.BLOCK_WIDTH:
                    self.y_vel *= -1
                elif block.y <= self.y <= block.y + block.BLOCK_HEIGHT:
                    self.x_vel *= -1
                break

        # If ball falls
        if self.y >= HEIGHT:
            scoreboard.lose_life()
            self.x = WIDTH // 2
            self.y = HEIGHT // 2 + 100
            self.x_vel = 0
            paddle.x = WIDTH // 2 - PADDLE_WIDTH // 2
            paddle.y = HEIGHT - PADDLE_HEIGHT - 10
            pygame.time.delay(200)