import pygame
from game import Game

pygame.mixer.init()

class Main:
    def __init__(self):

        self.window = pygame.display.set_mode([360, 640])
        pygame.display.set_caption("Flappy Dragon")

        pygame.mixer_music.load("assets/sounds/darkfantasy.mp3")
        pygame.mixer_music.play(-1)
        pygame.mixer.music.set_volume(0.05)

        icon = pygame.image.load("assets/dragons/dragon1.png")
        icon = pygame.transform.scale(icon, (32, 32))
        pygame.display.set_icon(icon)

        self.loop = True
        self.fps = pygame.time.Clock()

        self.game = Game()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False

    def draw(self):
        self.game.draw(self.window)
        self.game.update()

    def update(self):
        while self.loop:
            self.fps.tick(30)
            self.events()
            self.draw()
            pygame.display.flip()

Main().update()