import pygame
from player import Player
from setup import *
from tile import Tile

class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    # Create a Tile instance and add it to obstacle_sprites
                    tile = Tile((x, y), [self.obstacle_sprites, self.visible_sprites])
                elif col == 'p':
                    # Create a Player instance and add it to visible_sprites
                    player = Player((x, y))
                    self.visible_sprites.add(player)

    def run(self):
        # update and draw the game
        self.visible_sprites.draw(self.display_surface)
