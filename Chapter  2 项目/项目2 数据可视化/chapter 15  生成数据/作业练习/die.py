from random import randint

class Die():
    """表示一个骰子的类"""

    def __init__(self, num_sides = 6):
        """骰子默认的6面"""
        self.num_sides = num_sides


    def roll(self):
        """返回一个位于1和骰子面数之间的随机值"""
        # 函数randint就是返回一个1和面数之间的随机数
        return randint(1, self.num_sides)

    def random_num(self, number = 12):
        """表示的就是行坐标的值"""
        list = []
        for i in range(2,number+1):
            list.append(i)

        return list