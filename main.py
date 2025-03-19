import pygame
from game import Game
from menu import Menu

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
        self.menu = Menu()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if not self.menu.change_scene:
                self.menu.events(event)

    def draw(self):
        if not self.menu.change_scene:
            self.menu.draw(self.window)
            self.menu.update(str(self.game.max_score))
        elif not self.game.change_scene:
            self.game.draw(self.window)
            self.game.update()
        else:
            self.loop = False

    def update(self):
        while self.loop:
            self.fps.tick(30)
            self.events()
            self.draw()
            pygame.display.flip()

loop = True
while loop:
    Main().update()