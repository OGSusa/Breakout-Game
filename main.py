from paddle import Paddle
from ball import Ball
from block import Block
from scoreboard import Scoreboard
import pygame

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1200, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT, = 100, 20
BALL_RADIUS = 7


def draw(win, paddle, ball, blocks, scoreboard, game_over):
    win.fill(BLACK)

    paddle.draw(win)
    ball.draw(win)
    for block in blocks:
        block.draw(win)
    scoreboard.draw(win)

    if game_over:
        ball.x_vel = 0
        ball.y_vel = 0
        font = pygame.font.Font(None, 80)
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        win.blit(game_over_text, text_rect)

    pygame.display.update()


def handle_paddle_movement(keys, paddle):
    if keys[pygame.K_a] and paddle.x - paddle.VEL >= 0:
        paddle.move(left=True)
    if keys[pygame.K_d] and paddle.x + paddle.VEL + paddle.width <= WIDTH:
        paddle.move(left=False)


def main():
    run = True
    game_over = False
    clock = pygame.time.Clock()
    scoreboard = Scoreboard()

    paddle = Paddle(x=WIDTH // 2 - PADDLE_WIDTH // 2,
                    y=HEIGHT - PADDLE_HEIGHT - 10,
                    width=PADDLE_WIDTH,
                    height=PADDLE_HEIGHT)

    ball = Ball(x=WIDTH // 2,
                y=HEIGHT // 2 + 100,
                radius=BALL_RADIUS)

    blocks = []
    block_width = 60
    gap = 20
    padding = 2
    #Total width minus the padding
    usable_width = WIDTH - 2 * padding
    num_rows = 5
    max_blocks_in_row = (usable_width + padding) // (block_width + padding)

    #Generate the blocks
    for y in range(5):
        # Block is 60x20 + 20px gap
        row_positions = [(padding + i * (block_width + gap), 100 + y * 30) for i in range(max_blocks_in_row)]
        for i, (x, y_position) in enumerate(row_positions):
            hit_points = 5 - (y // 1)
            blocks.append(Block(x, y_position, hit_points))

    while run:
        clock.tick(FPS)
        draw(WIN, paddle, ball, blocks, scoreboard, game_over)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, paddle)

        ball.move(paddle, blocks, scoreboard)
        if scoreboard.lives <= 0:
            game_over = True

    pygame.quit()


if __name__ == "__main__":
    main()
