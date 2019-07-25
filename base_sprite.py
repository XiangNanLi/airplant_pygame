import pygame

class BaseSprite(pygame.sprite.Sprite):
    '''
    基础精灵
    '''

    def __init__(self, image, speed=1):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.speed = speed
    
    def update(self):
        # super().update()
        self.rect.y += self.speed