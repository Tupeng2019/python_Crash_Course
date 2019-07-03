'''
创建pygame窗口以及相应用户的输入
'''
import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化游戏并建立一个屏幕对象
    pygame.init()
    # 实例化，Settings
    ai_settings = Settings()
    # screen = pygame.display.set_mode((800, 600))
    # 这里后面的参数引发四是元组，而不是int整数型的，。所以要加上两个括号
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Ailen Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹色编组的实例
    bullets = Group()

    # 设置背景的颜色
    bg_color = (230, 230, 230)
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                #sys.exit()
        # 每一次循环时，都重绘制屏幕
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        ship.update()
        gf.update_bullets(bullets)
        # # 删除已经消失的子弹
        # for bullet in bullets.copy():
        #     if bullet.rect.bottom <=0:
        #         bullets.remove(bullet)
        # print(len(bullets))
        # # r让最近的绘制的屏幕可见
        # pygame.display.flip()
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()