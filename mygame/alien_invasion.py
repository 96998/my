import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # screen = pygame.display.set_mode((1200, 800))
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 设置背景色
    bg_color = (230, 230, 230)
    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        # bullets.update()
        # 删除已消失的子弹
        for bullet in bullets.copy():
            bullet.update()
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, bullets)
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        # 每次循环都重绘屏幕
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        # screen.fill(bg_color)
        # 让最近绘制的屏幕可见
        # pygame.display.flip()


if __name__ == '__main__':
    run_game()
