from obj import Obj, Tower, Coin, Dragon
import pygame
import random


class Game:
    def __init__(self):

        self.all_sprites = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()
        self.towers_group = pygame.sprite.Group()

        self.bg = Obj("assets/bg/layer_1.png", -180, 0, 320*3.6, 180*3.6, self.all_sprites)

        self.bg_2 = Obj("assets/bg/layer_2.png", 0, 260, 320*2, 131*2, self.all_sprites)
        self.bg_2_1 = Obj("assets/bg/layer_2.png", 640, 260, 320 * 2, 131 * 2, self.all_sprites)

        self.ground = Obj("assets/ground.png", 0, 400, 360, 360, self.all_sprites)
        self.ground_2 = Obj("assets/ground.png", 360, 400, 360, 360, self.all_sprites)

        self.dragon = Dragon("assets/dragons/dragon1.png", 10, 230, 144, 90, self.all_sprites)

        self.ticks = 0

    def draw(self, window):
        self.all_sprites.draw(window)

    def update(self):
        self.move_bg()
        self.all_sprites.update()

        if self.dragon.play:
            self.spawn_towers()
            self.dragon.collision_towers(self.towers_group)
            self.dragon.collision_coin(self.coin_group)

    def move_bg(self):
        self.bg_2.rect.x -= 1
        self.bg_2_1.rect.x -= 1
        if self.bg_2.rect.x <= -640:
            self.bg_2.rect.x = 0
        if self.bg_2_1.rect.x <= 0:
            self.bg_2_1.rect.x = 640

        self.ground.rect.x -= 5
        self.ground_2.rect.x -= 5

        if self.ground.rect.x <= -360:
            self.ground.rect.x = 0
        if self.ground_2.rect.x <= 0:
            self.ground_2.rect.x = 360

    def spawn_towers(self):
        self.ticks += 1

        if self.ticks >= random.randrange(80, 110):
            self.ticks = 0
            tower = Tower("assets/tower1.png", 360, random.randrange(300, 450), 82, 440, self.all_sprites, self.towers_group)
            tower_2 = Tower("assets/tower2.png", 360, tower.rect.y - 680, 82, 440, self.all_sprites, self.towers_group)
            coin = Coin("assets/coin/coin0.png", 395, tower.rect.y - 110, 17*2.6, 16*2.6, self.all_sprites, self.coin_group)

