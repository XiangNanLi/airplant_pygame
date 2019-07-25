import pygame
import random

import main

class EnemySprite(pygame.sprite.Group):
    '''
    Enemy Group内部存储enemy item
    '''

    class __EnemyItemSprite(pygame.sprite.Sprite):
        def __init__(self, level=0):
            '''
            敌机 level为随机的最高级别
            '''
            super().__init__()
            centerx = random.randint(29, main.SCREEN_WIDTH - 29)

            enemy_rect = pygame.Rect(534, 612, 57, 43)
            self.image = pygame.image.load('resources/images/shoot.png').subsurface(enemy_rect)
            self.rect = pygame.Rect(0,0, 57, 43)
            self.rect.centerx = centerx
            self.rect.bottom = 0
        
        def update(self):
            super().update()
            self.rect.bottom += 1
            if self.rect.top >= main.SCREEN_HIGHT :
                self.kill()

        def __del__(self):
            print('enemy item del')

    def __init__(self):
        super().__init__()
    
    def createEnemy(self):
        enemy = EnemySprite.__EnemyItemSprite()
        self.add(enemy)
    
    def update(self):
        super().update()
