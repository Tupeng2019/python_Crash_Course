
from die import Die
import matplotlib.pyplot as plt

die_1 = Die()
die_2 = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
#for roll_num in range(100):
# 增加次数，分析结果
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
'''这就是记录每一个点，出现的次数总和'''
#print(frequencies)

input_x = [ '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

plt.bar(input_x, frequencies, linewidth= 5)
# 设置图表标题，并给坐标轴加上标签
plt.title("D6 + D6", fontsize = 24)
plt.xlabel("Results", fontsize = 14)
plt.ylabel("frequencies", fontsize = 14)

# 设置刻度标记的大小
plt.tick_params(axis= 'both', labelsize = 14)
#lt.show()
plt.savefig('bar.png', bbox_inches = 'tight')