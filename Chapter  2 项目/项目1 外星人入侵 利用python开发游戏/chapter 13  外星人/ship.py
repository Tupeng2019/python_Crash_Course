import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        # 使用get_rect是获取相应的surface的属性rect，矩形
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每一艘新的飞船放在屏幕底部中央
        # centerx表示的就是飞船中心的x坐标点
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 在飞船的属性center中，存储小数值
        self.center = float(self.rect.centerx)
        # 移动标志,就是添加属性
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """根据移动标志来调整飞船的位置"""
        # 更新飞船的center值，而不是rect

        # self.rect.righr 返回的值就是飞船外接矩形的右边缘的x坐标
        if self.moving_right and self.rect.right <self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left >0:
            self.center -= self.ai_settings.ship_speed_factor

        # g根据self.center重新更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx