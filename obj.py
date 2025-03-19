import pygame

pygame.font.init()

class Obj(pygame.sprite.Sprite):
    def __init__(self, img, x, y, width = None, height = None, *groups):
        super().__init__(*groups)

        self.original_image = pygame.image.load(img)
        if width and height:
            self.original_image = pygame.transform.scale(self.original_image, (width, height))
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def drawing(self, window):
        pass

class Tower(Obj):
    def __init__(self, img, x, y, width = None, height = None, *groups):
        super().__init__(img, x, y, width, height,*groups)

    def update(self, *args):
        self.move()

    def move(self):
        self.rect.x -= 5

        if self.rect.x <= -82:
            self.kill()


class Coin(Obj):
    def __init__(self, img, x, y, width = None, height = None, *groups):
        super().__init__(img, x, y, width, height, *groups)

        self.ticks = 0

    def update(self, *args):
        self.move()
        self.anim()

    def move(self):
        self.rect.x -= 5

        if self.rect.x <= -82:
            self.kill()

    def anim(self):
        self.ticks = (self.ticks + 1) % 8
        self.image = pygame.image.load("assets/coin/coin" + str(self.ticks) + ".PNG")

class Dragon(Obj):
    def __init__(self, img, x, y, width = None, height = None, *groups):
        super().__init__(img, x, y, width, height, *groups)

        self.sound_hit = pygame.mixer.Sound("assets/sounds/hurt.mp3")
        self.sound_coin = pygame.mixer.Sound("assets/sounds/point.mp3")

        self.ticks = 0
        self.frame = 0
        self.vel = 4
        self.grav = 1

        self.pts = 0

        self.play = True

    def update(self, *args):

        self.move()

    def anim(self):
        self.ticks += 1

        if self.ticks >= 3:
            self.ticks = 0
            self.frame += 1

        if self.frame == 3:
            self.frame = 0

        self.image = pygame.image.load("assets/dragon" + str(self.frame) + ".PNG")

    def move(self):
        key = pygame.key.get_pressed()

        self.vel += self.grav
        self.rect.y += self.vel

        if self.vel >= 15:
            self.vel = 15
        if self.play:
            if key[pygame.K_SPACE]:
                self.anim()
                self.vel -= 3

        if self.rect.y >= 440:
            self.rect.y = 440
        elif self.rect.y <= -30:
            self.rect.y = -30
            self.vel = 4

    def collision_towers(self, group):

        col = pygame.sprite.spritecollide(self, group, False)

        if col:
            self.sound_hit.play()
            self.play = False

    def collision_coin(self, group):

        col = pygame.sprite.spritecollide(self, group, True)

        if col:
            self.sound_coin.play()
            self.pts += 1

class Text:
    def __init__(self, size, text):

        self.font = pygame.font.Font("assets/font/font.ttf", size)
        self.render = self.font.render(text, True, (255,255,255))

    def draw(self, window, x, y):
        window.blit(self.render, (x, y))

    def text_update(self, text):
        self.render = self.font.render(text, True, (255, 255, 255))