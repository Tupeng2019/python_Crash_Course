from random import choice

class RandomWalk():
    """生成一个随机漫步的类"""

    def __init__(self, num_points = 5000):
        """s初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有的随机漫步都始于（0,0）
        self.x_values = [0]
        self.y_values = [0]

    # def fill_walk(self):
    #     """计算随机漫步包含的所有的点"""
    #
    #     # 不断的漫步，直到表达式达到指定的长度
    #     while len(self.x_values) < self.num_points:
    #         # 决定前进方向以及延这个方向前进的距离
    #         # [1,-1]表示的就是要么向右走一，要么向左走一
    #         # 这既是15-4 所改的
    #         #x_direction = choice([1])
    #         x_direction = choice([1, -1])
    #         # 表示随机在0-4之间选择一个数作为走的距离
    #         x_distance = choice([0, 1, 2 ,3, 4])
    #         # 下面就是15-4所改
    #         #x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
    #         # 表示走的距离，如果为正，这就是要向上移动，如果为负下，为0 咋就是表示垂直运动
    #         x_step = x_direction *x_distance
    #
    #         y_direction = choice([1, -1])
    #         #y_distance = choice([0, 1, 2, 3, 4])
    #         y_distance = choice([0, 1, 2, 3, 4,5,6,7,8])
    #         y_step = y_direction * y_distance
    #
    #         # 拒绝原地踏步
    #         if x_step ==0 and y_step ==0:
    #             continue
    #
    #         # 计算下一次点的x和y的值
    #         next_x = self.x_values[-1] + x_step
    #         next_y = self.y_values[-1] + y_step
    #
    #         self.x_values.append(next_x)
    #         self.y_values.append(next_y)


    '''15-5 实现fill_walk的重构,--实际的效果还是不错的，说明是没有问题的'''

    def get_step(self):
        """计算随机漫步包含的所有的点"""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction *distance

    def fill_walk(self):

        # 不断的漫步，直到表达式达到指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及延这个方向前进的距离
            # [1,-1]表示的就是要么向右走一，要么向左走一
            # 这既是15-4 所改的
            #x_direction = choice([1])
            #x_direction = choice([1, -1])
            # 表示随机在0-4之间选择一个数作为走的距离
            #x_distance = choice([0, 1, 2 ,3, 4])
            # 下面就是15-4所改
            #x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            # 表示走的距离，如果为正，这就是要向上移动，如果为负下，为0 咋就是表示垂直运动
            #x_step = x_direction *x_distance

            #y_direction = choice([1, -1])
            #y_distance = choice([0, 1, 2, 3, 4])
            #y_distance = choice([0, 1, 2, 3, 4,5,6,7,8])
            #y_step = y_direction * y_distance

            # 调用刚刚重构的函数
            x_step = self.get_step()
            y_step = self.get_step()

            # 拒绝原地踏步
            if x_step ==0 and y_step ==0:
                continue

            # 计算下一次点的x和y的值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)