import pygame, sys, time
from settings import *

class Game:
    def __init__ (self):
        
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Flappy Plane')
        self.clock = pygame.time.Clock()
        
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        
    def run(self):
        last_time = time.time()
        while True:
            
            dt = time.time() - last_time
            last_time = time.time()
            
            for event in pygame.event.get():
                pygame.quit()
                sys.exit()
            
            pygame.display.update()
            self.clock.tick(FRAMERATE)

if __name__ == '__main__':
    game = Game()
    game.run()
