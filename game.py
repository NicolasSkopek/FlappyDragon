import pygame
from obj import Obj

class Game:
    def __init__(self):

        self.all_sprites = pygame.sprite.Group()


        self.bg = Obj("assets/bg/layer_1.png", -180, 0, 320*3.6, 180*3.6, self.all_sprites)
        self.bg_2 = Obj("assets/bg/layer_2.png", 0, 308, 320*2, 131*2, self.all_sprites)
        self.bg_2_1 = Obj("assets/bg/layer_2.png", 640, 308, 320 * 2, 131 * 2, self.all_sprites)

        self.ground = Obj("assets/ground.png", 0, 400, 360, 360, self.all_sprites)
        self.ground_2 = Obj("assets/ground.png", 360, 400, 360, 360, self.all_sprites)


    def draw(self, window):
        self.all_sprites.draw(window)

    def update(self):
        self.all_sprites.update()
        self.bg_2.rect.x -= 5
        self.bg_2_1.rect.x -= 5
        if self.bg_2.rect.x <= -640:
            self.bg_2.rect.x = 0
        if self.bg_2_1.rect.x <= 0:
            self.bg_2_1.rect.x = 640

        self.ground.rect.x -= 2
        self.ground_2.rect.x -= 2

        if self.ground.rect.x <= -360:
            self.ground.rect.x = 0
        if self.ground_2.rect.x <= 0:
            self.ground_2.rect.x = 360



