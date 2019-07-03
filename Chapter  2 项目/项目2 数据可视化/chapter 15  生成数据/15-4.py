import matplotlib.pyplot as plt

from random_walk import RandomWalk



while True:
    # 创建一个实例，并将其中包含的点，都绘制出来
    rw = RandomWalk()
    rw.fill_walk()

    # # 绘制窗口的尺寸
    # '''函数figure用于指定图表的宽度、高度、分辨率、和背景色'''
    # plt.figure(figsize = (10, 6))

    # 给点着色
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values,linewidth = 1)

    # 突出起点和终点
    plt.scatter(0,0 , c = 'green', edgecolors='none', s = 100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors='none',
                s = 100)
    # 隐藏坐标轴
    # 使用函数plt.axees()将每一条坐标轴的可见性设置为False
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk?(y/n):\n")
    if keep_running == 'n':
        break