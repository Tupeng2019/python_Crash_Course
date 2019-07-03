import json

#from __future__import (absolute_import, division,print_function, unicode_literals)

#这里就直接引用python3
#from urllib.request import urlopen
#
# import json
#
# json_url = 'http://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# response = urlopen(json_url)
# # 读取数据
# req = response.read()
# # 将数据写入文件
# with open('btc_close_2017_urllib.json', 'wb') as f:
#     f.write(req)
#
# # 加载json格式
# file.urllib = json.loads(req)
# print(file.urllib)



'''提取相关的信息'''
# # 将数据加载到一个列表当中
# filename = 'btc_close_2017.json'
# with open(filename) as f:
#     btc_data = json.load(f)
#
# # 打印每一条信息
# for btc_dict in btc_data:
#     date = btc_dict['date']
#     month = btc_dict['month']
#     week = btc_dict['week']
#     weekday = btc_dict['weekday']
#     close = btc_dict['close']
#     print("{}is month {} week{},{},the close price is {} RMB".format(date, month, week,
#                                                                      weekday,close))
#

'''将字符串转换为数字值   '''
# # 将数据加载到一个列表当中
# filename = 'btc_close_2017.json'
# with open(filename) as f:
#     btc_data = json.load(f)
#
# # 打印每一条信息
# for btc_dict in btc_data:
#     date = btc_dict['date']
#     month = int(btc_dict['month'])
#     week = int(btc_dict['week'])
#     weekday = btc_dict['weekday']
#     close = int(float(btc_dict['close']))
#     print("{}is month {} week{},{},the close price is {} RMB".format(date, month, week,
#                                                                      weekday, close))


'''绘制收盘价折线图'''
# # 将数据加载到一个列表当中
# filename = 'btc_close_2017.json'
# with open(filename) as f:
#     btc_data = json.load(f)
#
# # 创建五个列表，分别存储日期和收盘价
# dates = []
# months = []
# weeks = []
# weekday = []
# close = []
#
# # 打印每一条信息
# for btc_dict in btc_data:
#       dates.append(btc_dict['date'])
#       months.append(int(btc_dict['month']))
#       weeks.append(int(btc_dict['week']))
#       weekday.append(btc_dict['weekday'])
#       close.append(int(float(btc_dict['close'])))
#       #print("{}is month {} week{},{},the close price is {} RMB".format(dates, months, weeks,weekday, close))
#
# import pygal
#
# line_chart = pygal.Line(x_label_rotation = 20, show_minor_x_labels = False)
# line_chart.title = '收盘价'
# line_chart.x_labels = dates
# # x轴坐标每隔20太难显示一次
# N = 20
# line_chart.x_labels_major = dates[::N]
# line_chart.add('收盘价', close)
# line_chart.render_to_file('收盘价折线图.svg')


import math

'''时间序列特征初探 '''
# 将数据加载到一个列表当中
# filename = 'btc_close_2017.json'
# with open(filename) as f:
#     btc_data = json.load(f)
#
# # 创建五个列表，分别存储日期和收盘价
# dates = []
# months = []
# weeks = []
# weekday = []
# close = []
#
# # 打印每一条信息
# for btc_dict in btc_data:
#     dates.append(btc_dict['date'])
#     months.append(int(btc_dict['month']))
#     weeks.append(int(btc_dict['week']))
#     weekday.append(btc_dict['weekday'])
#     close.append(int(float(btc_dict['close'])))
#     #print("{}is month {} week{},{},the close price is {} RMB".format(dates, months, weeks,
#                                                                      weekday, close))
#
# import pygal
#
# line_chart = pygal.Line(x_label_rotation = 20, show_minor_x_labels = False)
# line_chart.title = '收盘价的对数变换'
# line_chart.x_labels = dates
# # x轴坐标每隔20太难显示一次
# N = 20
# line_chart.x_labels_major = dates[::N]
# close_log = [math.log10(i) for i in close]
# line_chart.add('log收盘价', close_log)
# line_chart.render_to_file('收盘价的对数变化折线图.svg')



'''收盘均价 '''
# 将数据加载到一个列表当中
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)

# 创建五个列表，分别存储日期和收盘价
dates = []
months = []
weeks = []
weekdays = []
close = []

# 打印每一条信息
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))
    print("{}is month {} week{},{},the close price is {} RMB".format(dates, months, weeks,
                                                                    weekdays, close))

'''f分别做一些特殊的图形'''
import pygal

line_chart = pygal.Line(x_label_rotation = 20, show_minor_x_labels = False)
line_chart.title = '收盘价的对数变换'
line_chart.x_labels = dates
# x轴坐标每隔20太难显示一次
N = 20
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(i) for i in close]
line_chart.add('log收盘价', close_log)
line_chart.render_to_file('收盘价的对数变化折线图.svg')



from itertools import groupby

def draw_line(x_data, y_data, title, y_legend):
     xy_map = []
     for x,y in groupby(sorted(zip(x_data, y_data)), key=lambda _:_[0]):
         y_list = [v for _ , v in y]
         xy_map.append([x, sum(y_list) / len(y_list)])
     x_unique, y_mean = [*zip(*xy_map)]
     line_chart = pygal.Line()
     line_chart.title = title
     line_chart.add(y_legend, y_mean)
     line_chart.render_to_file(title +'.svg')
     return line_chart

'''这既是收盘月日均价图'''
idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month], close[:idx_month], '收盘价约为均价', '月日均价')
line_chart_month


'''这就是周日均价图'''
idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(months[:idx_week], close[:idx_week], '收盘价周日为均价', '周日均价')
line_chart_week


'''做一些特殊的额处理'''
idx_week = dates.index('2017-12-11')
wd = ['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday','Saturday','Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]

line_chart_weekday = draw_line(weekdays_int, close[:idx_week], '收盘价星期为均价', '星期均价')
line_chart_weekday.x_labels = {'周一', '周二','周三','周四','周五', '周六','周日'}
line_chart_weekday.render_to_file('收盘价星期均值.svg')


'''收盘价数据仪表盘'''
with open('收盘价Dashboard.html', 'w', encoding='utf8') as html_file:
    html_file.write('<html><head><title>收盘价Dashbosrd</title><metacharset = "utf-8"></head><body>\n')
    for svg in [
        '收盘价折线图.svg', '收盘价的对数变化折线图.svg','收盘价均为均价.svg'
        '收盘价周日均价.svg','收盘价星期均值.svg'
    ]:
        html_file.write(' <object type = "image/svg + xml"data = "{0}" height = 500></object>\n'.format(svg))
    html_file.write('</body></html>')