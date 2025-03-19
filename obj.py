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


