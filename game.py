import pygame
from obj import Obj, Tower

class Game:
    def __init__(self):

        self.all_sprites = pygame.sprite.Group()


        self.bg = Obj("assets/bg/layer_1.png", -180, 0, 320*3.6, 180*3.6, self.all_sprites)

        self.bg_2 = Obj("assets/bg/layer_2.png", 0, 260, 320*2, 131*2, self.all_sprites)
        self.bg_2_1 = Obj("assets/bg/layer_2.png", 640, 260, 320 * 2, 131 * 2, self.all_sprites)

        self.ground = Obj("assets/ground.png", 0, 400, 360, 360, self.all_sprites)
        self.ground_2 = Obj("assets/ground.png", 360, 400, 360, 360, self.all_sprites)

        self.ticks = 0

    def draw(self, window):
        self.all_sprites.draw(window)

    def update(self):
        self.move_bg()
        self.spawn_towers()
        self.all_sprites.update()

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
        self.ticks += 0.5

        if self.ticks >= 30:
            self.ticks = 0
            tower = Tower("assets/tower1.png", 360, 320, 82, 196, self.all_sprites)
            tower_2 = Tower("assets/tower2.png", 360, -30, 82, 196, self.all_sprites)


