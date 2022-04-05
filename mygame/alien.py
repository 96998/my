import pygame
from pygame.sprite import Sprite


# 创建一个外星人类
class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        """初始化外星人并设置其位置"""
        super().__init__()
        # super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像并设置其位置
        self.image = pygame.image.load('./img/alien.bmp')
        self.rect = self.image.get_rect()

        # 每隔二外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
