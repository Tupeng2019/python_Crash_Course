import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    """显示得分信息的类"""

    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats


        # 显示得分信息是使用的字体设置
        self.text_color = (30, 30 , 30)
        self.font = pygame.font.SysFont(None, 48)


        # 准备初始化得分图形
        self.prep_score()

        # 准备包含最高得分和当前得分的图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

        self.prep_ships()


    def prep_score(self):
        """将得分转换为衣服渲染的图像"""
        '''
        函数round通常是让小数精确到小数点后面多少位，其中的小数点位数室友第二个实参是定的
        然后，如果第二个参数是负数，round函数就会将圆整到最近的10、100、1000等整数倍
        在python2中，round是返回的小数值，所以要用int
        而在python3中，这可以忽略int
        '''
        #rounded_score = int(round(self.stats.score, -1))
        rounded_score = round(self.stats.score, -1)
        # 将数值转换为字符串类型
        '''
        这里使用了 一个字符串格式设置的指令， 它让python将数值转换为字符串时在其中插入逗号，
        例如输出1,000,000而不是1000000，
        '''
        score_str = "{:,}".format(rounded_score)
        # 在将这个字符串传递给创建图像的render（）
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        # 这就是为了让得分的rect与屏幕的右边缘的始终相距10的像素
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 20


    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # 绘制飞船
        self.ships.draw(self.screen)


    def prep_high_score(self):
        """将最高的分装换为 渲染的图相"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,
                                                     self.ai_settings.bg_color)

        # 将最高的的分放在屏幕的顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """讲的及转换为渲染的图像"""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color,
                                            self.ai_settings.bg_color)

        # 将等级放在得分的下面
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """显示还剩余的飞船的数量"""
        # 创建一个空的编组用于存储飞船实例
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)