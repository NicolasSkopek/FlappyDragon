import pygame

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

        self.ticks = 0
        self.frame = 0

    def update(self, *args):
        self.anim()
        self.move()

    def anim(self):
        self.ticks += 1

        if self.ticks >= 3:
            self.ticks = 0
            self.frame += 1

        if self.frame == 3:
            self.frame = 0

        self.image = pygame.image.load("assets/dragons/dragon" + str(self.frame) + ".PNG")

    def move(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE]:
            print("VOAR")
