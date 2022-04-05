import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    # 这里用elif设置,则右键的优先级比左键高
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动飞船
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
        # if len(bullets) < ai_settings.bullet_allowed:
        #     new_bullet = Bullet(ai_settings, screen, ship)
        #     bullets.add(new_bullet)
    # 按下q也会退出游戏
    elif event.key == pygame.K_q:
        sys.exit()


# 创建函数update_bullets()
def update_bullets(bullets):
    """更新子弹的位置并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果没达到子弹上限,则发射一颗子弹"""
    if (len(bullets)) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, aliens):
    """创建外星人群"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    # 创建第一行外星人
    for alien_number in range(number_aliens_x):
        # 创建一个外星人并加入当前行
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets, aliens):
    """更新屏幕上的图像,并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw()
    ship.blitme()
    # alien.blitme()
    # Pygame自动绘制编组的每个元素
    aliens.draw(screen)
    # 让最近绘制的屏幕可见
    pygame.display.flip()
