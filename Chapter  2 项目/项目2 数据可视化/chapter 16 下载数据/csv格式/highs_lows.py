import csv

from matplotlib import pyplot as plt
from datetime import datetime

'''从文件中获取最高气温'''
# filename = 'sitka_weather_07-2014.csv'
# # 打开文件并存储数据
# with open(filename) as f:
#     '''reader 处理文件中以逗号隔开的第一行数据， 并将每一项数据
#               都作为一个元素存储在列表中 '''
#     reader = csv.reader(f)
#    '''next() 阅读器兑对象传递给他，并且将返回文件中的下一行
#        这里只是调用了一次，所以只是返回文件的第一行，其中包含
#       文件头 '''
#     header_row = next(reader)
#     #print(header_row)

#    '''打印文件头及其位置
#        在这里我们调用了  enumerate（） 来获取每一个元素的索引和它的值'''
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

#    '''获取最高的气温 '''
#     highs = []
#     for row in reader:
#         #highs.append(row[1])
#         '''下面就是使用int将这些字符串转换为数字'''
#         high = int(row[1])
#         highs.append(high)
#
#     print(highs)
#
'''根据数据绘制图形'''
# fig = plt.figure(dpi = 128, figsize=(10, 6))
# plt.plot(highs, c = 'red')
#
# # 设置图形的格式
# plt.title("Daily high twmperatures, july 2014", fontsize = 24)
# plt.xlabel(' ', fontsize = 16)
# plt.ylabel("Temperature(F)", fontsize = 16)
# plt.tick_params(axis='both', which = "major", labelsize = 16)
#
# plt.show()


'''在图表中添加日期'''
# # 从文件中获取最高气温和日期
# filename = 'sitka_weather_07-2014.csv'
# # 打开文件并存储数据
# with open(filename) as f:
#     '''reader 处理文件中以逗号隔开的第一行数据， 并将每一项数据
#               都作为一个元素存储在列表中 '''
#     reader = csv.reader(f)
#     '''next() 阅读器兑对象传递给他，并且将返回文件中的下一行
#        这里只是调用了一次，所以只是返回文件的第一行，其中包含
#        文件头 '''
#     header_row = next(reader)
#
#     dates, highs = [],[]
#     for row in reader:
#         current_date = datetime.strptime(row[0], "%Y-%m-%d")
#         dates.append(current_date)
#         high = int(row[1])
#         highs.append(high)
#
# '''根据数据绘制图形'''
# fig = plt.figure(dpi = 128, figsize=(10, 6))
# plt.plot(dates, highs, c = 'red')
# # plt.plot(highs, c = 'red')
#
# # 设置图形的格式
# plt.title("Daily high twmperatures, july 2014", fontsize = 24)
# plt.xlabel(' ', fontsize = 16)
# '''调用fig.autofmt_xdate 就是来绘制斜的标签，以免他们重复'''
# fig.autofmt_xdate()
# plt.ylabel("Temperature(F)", fontsize = 16)
# plt.tick_params(axis='both', which = "major", labelsize = 16)
#
# plt.show()


'''涵盖更长的时间'''
# # 从文件中获取最高气温和日期
# filename = 'sitka_weather_2014.csv'
# # 打开文件并存储数据
# with open(filename) as f:
#     '''reader 处理文件中以逗号隔开的第一行数据， 并将每一项数据
#               都作为一个元素存储在列表中 '''
#     reader = csv.reader(f)
#     '''next() 阅读器兑对象传递给他，并且将返回文件中的下一行
#        这里只是调用了一次，所以只是返回文件的第一行，其中包含
#        文件头 '''
#     header_row = next(reader)
#
#     dates, highs = [],[]
#     for row in reader:
#         current_date = datetime.strptime(row[0], "%Y-%m-%d")
#         dates.append(current_date)
#         high = int(row[1])
#         highs.append(high)
#
# '''根据数据绘制图形'''
# fig = plt.figure(dpi = 128, figsize=(10, 6))
# plt.plot(dates, highs, c = 'red')
# # plt.plot(highs, c = 'red')
#
# # 设置图形的格式
# plt.title("Daily high twmperatures - 2014", fontsize = 24)
# plt.xlabel(' ', fontsize = 16)
# '''调用fig.autofmt_xdate 就是来绘制斜的标签，以免他们重复'''
# fig.autofmt_xdate()
# plt.ylabel("Temperature(F)", fontsize = 16)
# plt.tick_params(axis='both', which = "major", labelsize = 16)
#
# plt.show()

'''在绘制一个数据系列'''
# # 从文件中获取最高气温、最低气温和日期
# filename = 'sitka_weather_2014.csv'
# # 打开文件并存储数据
# with open(filename) as f:
#     '''reader 处理文件中以逗号隔开的第一行数据， 并将每一项数据
#               都作为一个元素存储在列表中 '''
#     reader = csv.reader(f)
#     '''next() 阅读器兑对象传递给他，并且将返回文件中的下一行
#        这里只是调用了一次，所以只是返回文件的第一行，其中包含
#        文件头 '''
#     header_row = next(reader)
#
#     dates, highs, lows = [],[], []
#     for row in reader:
#         current_date = datetime.strptime(row[0], "%Y-%m-%d")
#         dates.append(current_date)
#         high = int(row[1])
#         highs.append(high)
#
#         low = int(row[3])
#         lows.append(low)
#
# '''根据数据绘制图形'''
# fig = plt.figure(dpi = 128, figsize=(10, 6))
# plt.plot(dates, highs, c = 'red')
# plt.plot(dates, lows, c = 'blue')
#
# # plt.plot(highs, c = 'red')
#
# # 设置图形的格式
# plt.title("Daily high and low twmperatures - 2014", fontsize = 24)
# plt.xlabel(' ', fontsize = 16)
# '''调用fig.autofmt_xdate 就是来绘制斜的标签，以免他们重复'''
# fig.autofmt_xdate()
# plt.ylabel("Temperature(F)", fontsize = 16)
# plt.tick_params(axis='both', which = "major", labelsize = 16)
#
# plt.show()


'''给图表区域着色'''
# # 从文件中获取最高气温、最低气温和日期
# filename = 'sitka_weather_2014.csv'
# # 打开文件并存储数据
# with open(filename) as f:
#     '''reader 处理文件中以逗号隔开的第一行数据， 并将每一项数据
#               都作为一个元素存储在列表中 '''
#     reader = csv.reader(f)
#     '''next() 阅读器兑对象传递给他，并且将返回文件中的下一行
#        这里只是调用了一次，所以只是返回文件的第一行，其中包含
#        文件头 '''
#     header_row = next(reader)
#
#     dates, highs, lows = [],[], []
#     for row in reader:
#         current_date = datetime.strptime(row[0], "%Y-%m-%d")
#         dates.append(current_date)
#         high = int(row[1])
#         highs.append(high)
#
#         low = int(row[3])
#         lows.append(low)
#
# '''根据数据绘制图形'''
# fig = plt.figure(dpi = 128, figsize=(10, 6))
# plt.plot(dates, highs, c = 'red', alpha = 0.5)
# plt.plot(dates, lows, c = 'blue', alpha = 0.5)
# '''给指定区域填充颜色'''
# # 这里的alpha就是指的是透明度， 如果等于0，就是表示完全透明的
# plt.fill_between(dates, highs, lows, facecolor = 'green', alpha = 0.5)
# # plt.plot(highs, c = 'red')
#
# # 设置图形的格式
# plt.title("Daily high and low twmperatures - 2014", fontsize = 24)
# plt.xlabel(' ', fontsize = 16)
# '''调用fig.autofmt_xdate 就是来绘制斜的标签，以免他们重复'''
# fig.autofmt_xdate()
# plt.ylabel("Temperature(F)", fontsize = 16)
# plt.tick_params(axis='both', which = "major", labelsize = 16)
#
# plt.show()


'''错误检查 
   有时候数据会出现 - 未能收集部分数据和全部应该收集的数据，
   缺失的数据偶尔出现错误，引发可能出现的异常，所以哟啊及时
   的进行错误处理'''
# 从文件中获取最高气温、最低气温和日期
filename = 'death_valley_2014.csv'
# 打开文件并存储数据
with open(filename) as f:
    '''reader 处理文件中以逗号隔开的第一行数据， 并将每一项数据
              都作为一个元素存储在列表中 '''
    reader = csv.reader(f)
    '''next() 阅读器兑对象传递给他，并且将返回文件中的下一行
       这里只是调用了一次，所以只是返回文件的第一行，其中包含
       文件头 '''
    header_row = next(reader)

    dates, highs, lows = [],[], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            #dates.append(current_date)
            high = int(row[1])
            #highs.append(high)

            low = int(row[3])
            #lows.append(low)
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

'''根据数据绘制图形'''
fig = plt.figure(dpi = 128, figsize=(10, 6))
plt.plot(dates, highs, c = 'red', alpha = 0.5)
plt.plot(dates, lows, c = 'blue', alpha = 0.5)
'''给指定区域填充颜色'''
# 这里的alpha就是指的是透明度， 如果等于0，就是表示完全透明的
plt.fill_between(dates, highs, lows, facecolor = 'green', alpha = 0.5)
# plt.plot(highs, c = 'red')

# 设置图形的格式
plt.title("Daily high and low twmperatures - 2014\nDeath valley, CA", fontsize = 24)
plt.xlabel(' ', fontsize = 16)
'''调用fig.autofmt_xdate 就是来绘制斜的标签，以免他们重复'''
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize = 16)
plt.tick_params(axis='both', which = "major", labelsize = 16)

plt.show()