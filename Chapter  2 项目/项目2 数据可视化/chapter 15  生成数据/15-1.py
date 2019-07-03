import matplotlib.pyplot as plt

n = int(input("please input this number:"))
x_values = list(range(1,n+1))
y_values = [x**3 for x in x_values]

#plt.scatter(x_values, y_values,c= 'red', edgecolor = 'none', s= 40)

# 添加颜色映射,在这里颜色的单词的末尾都是要加s的
plt.scatter(x_values, y_values,c= y_values,cmap=plt.cm.Greens, edgecolor = 'none', s= 40)

# 设置图表标题并给坐标轴加上个标签
plt.title("**3  Number", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Squares of Value", fontsize = 14)

# 设置每一个坐标轴的取值范围-- 函数axis就是该作用的，并且要求提供4个值
plt.axis([0, 100, 0, 1100000])

plt.show()