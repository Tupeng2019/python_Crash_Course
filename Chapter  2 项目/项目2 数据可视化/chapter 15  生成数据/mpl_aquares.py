import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
#plt.plot(squares)
# 修改线条的粗细
#plt.plot(squares, linewidth= 5)
# 由于刚刚的输出没有呢么准确所以现在就引入新的输入值，就是下标
plt.plot(input_values, squares, linewidth= 5)
# 设置图表标题，并给坐标轴加上标签
plt.title("Aquares Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Squares of Value", fontsize = 14)

# 设置刻度标记的大小
plt.tick_params(axis= 'both', labelsize = 14)
plt.show()