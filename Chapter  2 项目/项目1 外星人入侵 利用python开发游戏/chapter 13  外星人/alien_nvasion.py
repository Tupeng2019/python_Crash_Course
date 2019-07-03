'''
创建pygame窗口以及相应用户的输入
'''
import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
#from alien import Alien
import game_functions as gf
from game_stats import GameStats

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

    # 创建一个哟用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一个外星人
    #alien = Alien(ai_settings, screen)
    # 创建一个用于存储子弹色编组的实例
    bullets = Group()
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

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
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings,stats, screen,ship, aliens, bullets)
            # # 删除已经消失的子弹
            # for bullet in bullets.copy():
            #     if bullet.rect.bottom <=0:
            #         bullets.remove(bullet)
            # print(len(bullets))
            # # r让最近的绘制的屏幕可见
            # pygame.display.flip()
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()