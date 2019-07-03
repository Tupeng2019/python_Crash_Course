from django.db import models

# Create your models here.
# 在这里创建模型
class Topic(models.Model):
    """用户学习的主题"""
    # 这就是必须告诉数据库中药预留的多少空间，既是200个字符
    text = models.CharField(max_length= 200)
    #这就是用来记录日期和时间的数据
    date_added = models.DateTimeField(auto_now_add=True)

    # 显示模型的简单表示
    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
    """学到的有关某个主题的具体指示"""
    topic = models.ForeignKey(Topic, on_delete= models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add= True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50]+ '...'