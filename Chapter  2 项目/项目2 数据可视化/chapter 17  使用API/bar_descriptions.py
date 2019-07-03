import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

'''添加自定义工具提示'''
#将基色设置为深蓝色
my_style = LS('#333366', base_style = LCS)
# 想x轴旋转45度，并且隐藏图例
chart = pygal.Bar(style = my_style, x_label_rotaiton = 45, show_legend = False)

chart.title = 'Python Project'
chart.x_labels = ['httpie','django','flask']

plot_dicts = [
    {'value': 16101, 'label': 'Description of httpie'},
    {'value': 15028, 'label': 'Description of django'},
    {'value': 14798, 'label': 'Description of flask'},
]
# 方法add是接受一个字符串和一个列表的
chart.add('',plot_dicts)
chart.render_to_file('bar_descriptions.svg')