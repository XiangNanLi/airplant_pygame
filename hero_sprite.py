import pygame

from main import *

HERO_SPEED = 1
SHOOT_SPEED = 2

class HeroSprite(pygame.sprite.Group):
    '''
    英雄group
    '''

    class __Hero(pygame.sprite.Sprite):
        '''
        英雄
        '''

        def __init__(self):
            super().__init__()
            self.image = pygame.image.load('resources/images/shoot.png').subsurface(pygame.Rect(0, 99, 102, 126))
            self.rect = pygame.Rect(0,0,102,126)
            self.rect.centerx = SCREEN_WIDTH/2.0
            self.rect.bottom = SCREEN_HIGHT - 10

        def move(self, direction = 0):
            hero_rect = self.rect
            if direction == 0: # move left
                hero_rect.left -= HERO_SPEED
                if hero_rect.left <= 0:
                    hero_rect.left = 0
            else: # move right
                hero_rect.right += HERO_SPEED
                if hero_rect.right >= SCREEN_WIDTH:
                    hero_rect.right = SCREEN_WIDTH
        
        def update(self):
            super().update()
            # Hero移动
            # if self.rect.bottom <= 0:
            #     self.rect.top = SCREEN_HIGHT
            # else:
            #     self.rect.top -= 1


    class __HeroBullet(pygame.sprite.Sprite):
        '''
        英雄子弹
        '''
        
        def __init__(self):
            super().__init__()
            bullet_rect = pygame.Rect(69, 78, 9, 21)
            self.image = pygame.image.load('resources/images/shoot.png').subsurface(bullet_rect)
            self.rect = pygame.Rect(0, 0, 9, 21)
        
        def update(self):
            super().update()
            # 子弹移动
            if self.rect.bottom <= 0:
                self.kill()
            else:
                self.rect.top -= 3
    
    def __init__(self):
        super().__init__()

        # Hero制作
        self.hero = HeroSprite.__Hero()
        self.add(self.hero)
        
        # 子弹
        self.bullets = pygame.sprite.Group()
        # self.add(self.bullets)

    def shoot(self):
        hero_rect = self.hero.rect
        bullet = HeroSprite.__HeroBullet()
        bullet.rect.centerx = hero_rect.centerx
        bullet.rect.bottom = hero_rect.top
        self.bullets.add(bullet)
    
    def move(self, direction=0):
        self.hero.move(direction)

    def update(self):
        super().update()

        
