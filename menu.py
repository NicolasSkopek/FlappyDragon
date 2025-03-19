from obj import Obj, Text
import pygame

class Menu:

    def __init__(self):
        self.all_sprites = pygame.sprite.Group()

        self.bg = Obj("assets/bg/layer_1.png", -180, 0, 320 * 3.6, 180 * 3.6, self.all_sprites)

        self.bg_2 = Obj("assets/bg/layer_2.png", 0, 260, 320 * 2, 131 * 2, self.all_sprites)
        self.bg_2_1 = Obj("assets/bg/layer_2.png", 640, 260, 320 * 2, 131 * 2, self.all_sprites)

        self.ground = Obj("assets/ground.png", 0, 400, 360, 360, self.all_sprites)
        self.ground_2 = Obj("assets/ground.png", 360, 400, 360, 360, self.all_sprites)

        self.get_ready = Obj("assets/getready.png", 80, 140, 615/3, 141/3, self.all_sprites)
        self.table_score = Obj("assets/score.png", 50, 230, 523/2, 361/2, self.all_sprites)
        self.button_go = Obj("assets/go.png", 120, 415, 439/4, 181/4, self.all_sprites)

        self.change_scene = False

        self.text_score = Text(100, "0")

    def draw(self, window):
        self.all_sprites.draw(window)
        self.text_score.draw(window, 145, 290)

    def update(self, pts):
        self.all_sprites.update()
        self.move_bg()
        self.text_score.text_update(pts)

    def events(self,event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self.button_go.rect.collidepoint(pygame.mouse.get_pos()):
                self.change_scene = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.change_scene = True


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