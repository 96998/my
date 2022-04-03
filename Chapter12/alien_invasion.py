import sys
import pygame
import settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    """创建游戏窗口"""
    pygame.init()
    # screen = pygame.display.set_mode((1200, 800))
    # pygame.display.set_caption('Alien Invasion')
    ai_settings = settings.Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.caption)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 设置背景色
    bg_color = (230, 230, 230)
    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, bullets)
    # while True:
    #     # 监视键盘和鼠标事件
    #     for event in pygame.event.get():
    #         # 鼠标点击X的时候关闭
    #         if event.type == pygame.QUIT:
    #             sys.exit()
    #
    #     # 每次循环都重绘屏幕
    #     screen.fill(bg_color)
    #     # 绘制飞船
    #     ship.blitme()
    #     # 使最近的绘制可见,不断更新屏幕
    #     pygame.display.flip()


if __name__ == '__main__':
    run_game()
