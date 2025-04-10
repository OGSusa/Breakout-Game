import pygame


class Block:
    BLOCK_WIDTH = 75
    BLOCK_HEIGHT = 28
    COLOR_5 = (16, 17, 109)
    COLOR_4 = (42, 53, 139)
    COLOR_3 = (68, 88, 169)
    COLOR_2 = (94, 124, 199)
    COLOR_1 = (120, 160, 230)

    def __init__(self, x, y, hit_points):
        self.x = x
        self.y = y
        self.hit_points = hit_points

    def draw(self, win):
        # The more hp a block has the darker the color will be
        colors = [self.COLOR_1, self.COLOR_2, self.COLOR_3, self.COLOR_4, self.COLOR_5]
        if 1 <= self.hit_points <= 5:
            pygame.draw.rect(win, colors[self.hit_points - 1], (self.x, self.y, self.BLOCK_WIDTH, self.BLOCK_HEIGHT))

    def gets_hit(self, blocks):
        # Reduces the hp of the block and changes the color
        if self.hit_points > 0:
            self.hit_points -= 1
        if self.hit_points == 0:
            self.destroy(blocks)

    def destroy(self, blocks):
        # Remove the block from the list
        if self in blocks:
            blocks.remove(self)
