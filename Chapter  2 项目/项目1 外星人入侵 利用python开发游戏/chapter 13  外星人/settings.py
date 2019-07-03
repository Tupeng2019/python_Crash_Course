'''
创建设置类
'''
class Settings():
    """存储 <外星人入侵>的所有设置类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230,230,230)

        # 飞船的速度设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3


        # 子弹的设置
        # 设置的是 宽为3个像素，高唯15个像素的深灰色子弹
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

        # 外星人的设置
        self.alien_speed_factor = 1
        # 表示撞到屏幕边缘时，反方向下降到的速度
        self.fleet_drop_speed = 10
        # fleet_direction 为1表示向右移动，为-1就是表示向左移动
        self.fleet_direction = 1