import matplotlib.pyplot as plt

#plt.scatter(2, 4)
# 实参表示绘制图像时使用的点的尺寸
#plt.scatter(2, 4,s = 200)


'''
绘制一系列的点
'''

'''
x_label = [1, 2, 3, 4, 5  ]
y_label = [1, 4, 9, 16, 25 ]
plt.scatter(x_label, y_label, s = 100)
# 设置图表标题并给坐标轴加上个标签
plt.title("Squares Number", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Squares of Value", fontsize = 14)

# 设置刻度标记的大小
plt.tick_params(axis= 'both', which = 'major', labelsize = 14)
plt.show()
'''

'''
自动计算数据
'''
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
# 还可以进行删除数据点的轮廓
#plt.scatter(x_values, y_values, s = 40)
#plt.scatter(x_values, y_values, edgecolor = 'none', s= 40)

# 传递颜色，实参c就是代表的颜色
#plt.scatter(x_values, y_values,c= 'red', edgecolor = 'none', s= 40)

# 使用颜色映射colormap
plt.scatter(x_values, y_values,c= y_values,cmap=plt.cm.Blues, edgecolor = 'none', s= 40)

# 设置图表标题并给坐标轴加上个标签
plt.title("Squares Number", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Squares of Value", fontsize = 14)

# 设置每一个坐标轴的取值范围-- 函数axis就是该作用的，并且要求提供4个值
plt.axis([0, 1100, 0, 1100000])

#plt.show()

# 自动保存图表
'''第一个参数既是表示该图标保存的文件名字，第二个参数就是表示的删除图表多余的空白的地方，
   当然可以不用这个参数了'''
plt.savefig('squares_plt.png', bbox = 'tight')