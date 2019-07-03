# import requests
#
# # 执行API调并存储响应
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
# print("Status code:", r.status_code)
#
# # 将API响应存储在一个变量中
# response_dict = r.json()
#
# # 处理结果
# #print(reponses_dict.keys())
#
# '''处理响应字典'''
# print("Total repositories:", response_dict['total_count'])
#
# #探索有关创库的信息
# repo_dicts = response_dict['items']
# print("Respositores returned:", len(repo_dicts))

# 研究第一个仓库
#repo_dict = repo_dicts[0]

# print("\nKeys:", len(repo_dict))
# # for key in sorted(repo_dict.keys()):
# #     print(key)

'''打印第一个仓库的信息'''
# print("\nSelected information about first repository:")
#
# print('name:', repo_dict['name'])
# print('Owner:', repo_dict['owner']['login'])
# print('Stars:', repo_dict['stargazers_count'])
# print('Repository:', repo_dict['html_url'])
# print('Created:', repo_dict['created_at'])
# print('Updated:', repo_dict['updated_at'])
# print('Description:', repo_dict['description'])


'''概述最受欢迎的仓库'''
# print("\nSelected information about each repository:")
# for repo_dict in repo_dicts:
#
#     print('name:', repo_dict['name'])
#     print('Owner:', repo_dict['owner']['login'])
#     print('Stars:', repo_dict['stargazers_count'])
#     print('Repository:', repo_dict['html_url'])
#     print('Description:', repo_dict['description'])



'''监视API的速率限制'''
'''https://api.github.com/rate_limit  直接在网页中输入下面的地址就好了'''


'''使用pygal可视化仓库'''

# import pygal
# from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
# import requests
#
# # 执行API调并存储响应
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
# print("Status code:", r.status_code)
#
# # 将API响应存储在一个变量中
# response_dict = r.json()
#
# # 处理结果
# #print(reponses_dict.keys())
#
# '''处理响应字典'''
# print("Total repositories:", response_dict['total_count'])
#
# #探索有关创库的信息
# repo_dicts = response_dict['items']
# #print("Respositores returned:", len(repo_dicts))
# # 用于存储图表信息
# names, stars = [], []
# for repo_dict in repo_dicts:
#     names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])
#
# # 实现可视化
# #将基色设置为深蓝色
# my_style = LS('#333366', base_style = LCS)
# # 想x轴旋转45度，并且隐藏图例
# chart = pygal.Bar(style = my_style, x_label_rotaiton = 45, show_legend = False)
# chart.title = 'Most-Starred Python Project on github'
# chart.x_labels = names
#
# chart.add('', stars)
# chart.render_to_file('python_repo.svg')


'''改进PYgal图表 ###'''
# import pygal
# from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
# import requests
#
# # 执行API调并存储响应
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
# print("Status code:", r.status_code)
#
# # 将API响应存储在一个变量中
# response_dict = r.json()
#
# # 处理结果
# #print(reponses_dict.keys())
#
# '''处理响应字典'''
# print("Total repositories:", response_dict['total_count'])
#
# #探索有关创库的信息
# repo_dicts = response_dict['items']
# #print("Respositores returned:", len(repo_dicts))
# # 用于存储图表信息
# names, stars = [], []
# for repo_dict in repo_dicts:
#     names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])
#
# # 实现可视化
# #将基色设置为深蓝色
# my_style = LS('#333366', base_style = LCS)
#
# my_config = pygal.Config()
# my_config.x_label_rotation = 45
# # 这就是隐藏图表中的水平线
# my_config.show_legend = False
# my_config.title_font_size = 24
# my_config.label_font_size = 14
# my_config.major_label_font_size = 18
# # 将较长的项目名缩短为15个字符
# my_config.truncate_label = 15
# my_config.show_y_guides = False
# # 设置自定义宽度
# my_config.width = 1000
# # 想x轴旋转45度，并且隐藏图例
# chart = pygal.Bar(my_config, style = my_style)
# chart.title = 'Most-Starred Python Project on github'
# chart.x_labels = names
#
# chart.add('', stars)
# chart.render_to_file('python_repos.svg')


'''### 根据数据绘制图 #####'''
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import requests

# 执行API调并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()

# 处理结果
#print(reponses_dict.keys())

'''处理响应字典'''
print("Total repositories:", response_dict['total_count'])

#探索有关创库的信息
repo_dicts = response_dict['items']
#print("Respositores returned:", len(repo_dicts))
# 用于存储图表信息
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])    #stars.append(repo_dict['stargazers_count'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        # 因为description的内容是字符串的形式，所以前面要加str方法
        'label': str(repo_dict['description']),
        '''在图标中添加课单击的连接'''
        'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

# 实现可视化
#将基色设置为深蓝色
my_style = LS('#333366', base_style = LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
# 这就是隐藏图表中的水平线
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
# 将较长的项目名缩短为15个字符
my_config.truncate_label = 15
my_config.show_y_guides = False
# 设置自定义宽度
my_config.width = 1000
# 想x轴旋转45度，并且隐藏图例
chart = pygal.Bar(my_config, style = my_style)
chart.title = 'Most-Starred Python Project on github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos_es.svg')