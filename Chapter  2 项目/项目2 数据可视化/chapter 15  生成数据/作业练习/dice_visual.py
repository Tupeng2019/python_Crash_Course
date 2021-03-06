import pygal
from die import Die

'''同时掷两个骰子'''
# 创建一个D6实例
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

'''对结果进行可视化  ----利用直方图Bar()来可视化 '''
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times "
#hist.x_labels = [ '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
# 这里直接运用列表的形式就好了。不用什么str来转换了
labels = die_1.random_num()
hist.x_labels = labels
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')