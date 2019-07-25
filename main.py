import random
import pygame
import sys

from background_sprite import *
from base_sprite import *
from hero_sprite import *
from enemy_sprite import *

SCREEN_WIDTH = 480
SCREEN_HIGHT = 800
# 创建Enemy事件
ENEMYCREATEEVENTID = pygame.USEREVENT
# 创建子弹事件
HEROBULLETCREATEEVENTID = pygame.USEREVENT + 1

if __name__ == "__main__":
    # 初始化
    pygame.init()
    # 定义屏幕大小
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
    # 定义时钟
    clock = pygame.time.Clock()

    # 背景Sprite
    ground_group = BackgroundSprite('resources/images/background.png')
    # 创建英雄
    hero = HeroSprite()
    # 创建敌机
    enemy = EnemySprite()

    # 创建敌机
    pygame.time.set_timer(ENEMYCREATEEVENTID, 1000)
    # 创建子弹
    pygame.time.set_timer(HEROBULLETCREATEEVENTID, 200)

    while True:
        # 设定时钟频率
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT : # 退出游戏
                pygame.quit()
                exit()
            elif event.type == ENEMYCREATEEVENTID: # 创建敌机
                enemy.createEnemy()
            elif event.type == HEROBULLETCREATEEVENTID: # 创建子弹
                hero.shoot()

        press_keys = pygame.key.get_pressed() # 获取按键
        if press_keys[pygame.K_LEFT]:
            hero.move(0)
        elif press_keys[pygame.K_RIGHT]:
            hero.move(1)   

        # 背景更新/绘制
        ground_group.update()
        ground_group.draw(screen)

        # 英雄绘制
        hero.update()
        hero.bullets.update()
        hero.draw(screen)
        hero.bullets.draw(screen)

        # 敌机绘制
        enemy.update()
        enemy.draw(screen)

        # 子弹打中敌机
        pygame.sprite.groupcollide(enemy, hero.bullets, True, True, collided = None)
        # 敌机碰撞英雄
        sprites = pygame.sprite.spritecollide(hero.hero, enemy, True, collided = None) 
        if len(sprites) > 0:
            print("Game over")

        pygame.display.update()