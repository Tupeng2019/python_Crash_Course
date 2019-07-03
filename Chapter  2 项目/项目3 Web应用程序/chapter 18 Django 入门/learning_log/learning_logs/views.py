from django.shortcuts import render

from .models import Topic
# Create your views here.
# 在这里建立试图
def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """显示多余的主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics' : topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request,topic_id):
    """显示单个的主题以及所有的条目"""
    # 按属性进行升序排列
    '''下面两行的代码都是表示查询'''
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)