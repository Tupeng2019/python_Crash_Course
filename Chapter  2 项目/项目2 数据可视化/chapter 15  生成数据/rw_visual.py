import matplotlib.pyplot as plt

from random_walk import RandomWalk

'''
# 创建一个实例，并将其中包含的点，都绘制出来
rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s = 15)

plt.show()

'''

"""模拟多次随机漫步的结果"""
# 只要程序处于活动状态，就不断的模拟随机漫步
# while True:
#     # 创建一个实例，并将其中包含的点，都绘制出来
#     rw = RandomWalk()
#     rw.fill_walk()
#     plt.scatter(rw.x_values, rw.y_values, s=15)
#     plt.show()
#
#     keep_running = input("Make another walk?(y/n):\n")
#     if keep_running == 'n':
#         break

'''增加了新的功能，就是给点着色'''
# while True:
#     # 创建一个实例，并将其中包含的点，都绘制出来
#     rw = RandomWalk()
#     rw.fill_walk()
#
#     # 给点着色
#     point_numbers = list(range(rw.num_points))
#     plt.scatter(rw.x_values, rw.y_values,c = point_numbers, cmap= plt.cm.Blues,
#                 edgecolors='none', s=15)
#     plt.show()
#
#     keep_running = input("Make another walk?(y/n):\n")
#     if keep_running == 'n':
#         break


'''重新绘制起点和终点'''
# while True:
#     # 创建一个实例，并将其中包含的点，都绘制出来
#     rw = RandomWalk()
#     rw.fill_walk()
#
#     # 给点着色
#     point_numbers = list(range(rw.num_points))
#     plt.scatter(rw.x_values, rw.y_values,c = point_numbers, cmap= plt.cm.Blues,
#                 edgecolors='none', s=15)
#
#     # 突出起点和终点
#     plt.scatter(0,0 , c = 'green', edgecolors='none', s = 100)
#     plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors='none',
#                 s = 100)
#     plt.show()
#
#     keep_running = input("Make another walk?(y/n):\n")
#     if keep_running == 'n':
#         break

'''隐藏坐标轴'''
while True:
    # 创建一个实例，并将其中包含的点，都绘制出来
    rw = RandomWalk()
    rw.fill_walk()

    # 给点着色
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values,c = point_numbers, cmap= plt.cm.Blues,
                edgecolors='none', s=15)

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


'''增加点数'''
# while True:
#     # 创建一个实例，并将其中包含的点，都绘制出来
#     rw = RandomWalk(50000)
#     rw.fill_walk()
#
#     # 给点着色
#     point_numbers = list(range(rw.num_points))
#     plt.scatter(rw.x_values, rw.y_values,c = point_numbers, cmap= plt.cm.Blues,
#                 edgecolors='none', s=1)
#
#     # 突出起点和终点
#     plt.scatter(0,0 , c = 'green', edgecolors='none', s = 100)
#     plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors='none',
#                 s = 100)
#     # 隐藏坐标轴
#     # 使用函数plt.axees()将每一条坐标轴的可见性设置为False
#     plt.axes().get_xaxis().set_visible(False)
#     plt.axes().get_yaxis().set_visible(False)
#
#     plt.show()
#
#     keep_running = input("Make another walk?(y/n):\n")
#     if keep_running == 'n':
#         break


'''调整尺寸以适应屏幕'''
# while True:
#     # 创建一个实例，并将其中包含的点，都绘制出来
#     rw = RandomWalk()
#     rw.fill_walk()
#
#     # 绘制窗口的尺寸
#     '''函数figure用于指定图表的宽度、高度、分辨率、和背景色'''
#     plt.figure(figsize = (10, 6))
#
#     # 给点着色
#     point_numbers = list(range(rw.num_points))
#     plt.scatter(rw.x_values, rw.y_values,c = point_numbers, cmap= plt.cm.Blues,
#                 edgecolors='none', s=15)
#
#     # 突出起点和终点
#     plt.scatter(0,0 , c = 'green', edgecolors='none', s = 100)
#     plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors='none',
#                 s = 100)
#     # 隐藏坐标轴
#     # 使用函数plt.axees()将每一条坐标轴的可见性设置为False
#     plt.axes().get_xaxis().set_visible(False)
#     plt.axes().get_yaxis().set_visible(False)
#
#     plt.show()
#
#     keep_running = input("Make another walk?(y/n):\n")
#     if keep_running == 'n':
#         break