import pygame

class BackgroundSprite(pygame.sprite.Group):

    def __init__(self, image_path):
        super().__init__()

        image = pygame.image.load(image_path)
        image_rect = image.get_rect() # 获取图像宽高

        self.bg1 = pygame.sprite.Sprite()
        self.bg1.image = image
        self.bg1.rect = image_rect
        self.add(self.bg1)

        self.bg2 = pygame.sprite.Sprite()
        self.bg2.image = image
        self.bg2.rect = pygame.Rect(0, image_rect.height, image_rect.width, image_rect.height)
        self.add(self.bg2)

        self.__image = image
        self.__image_rect = image_rect

    def update(self):
        super().update()
        if self.bg1.rect.bottom <= 0:
            self.bg1.rect.top = self.__image_rect.height
        else:
            self.bg1.rect.top -= 1
        
        if self.bg2.rect.bottom <= 0:
            self.bg2.rect.top = self.__image_rect.height
        else:
            self.bg2.rect.top -= 1