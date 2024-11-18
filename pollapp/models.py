from django.db import models
from django.contrib.auth.models import User
import random

# 数据库中创建两个table
class Poll(models.Model):
    # 投票问题部分的元素： title, description, 创建者， 创建时间，结束时间
    title = models.CharField(max_length=200)  # 投票标题
    description = models.TextField(blank=True, null=True)  # 投票描述
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # 创建者
    created_at = models.DateTimeField(auto_now_add=True)  # 创建时间
    end_date = models.DateTimeField()  # 投票结束时间

class Choice(models.Model):
    # 选择部分的元素：和poll连接，choice, 投票数
    poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)  # 选项内容
    votes = models.IntegerField(default=0)  # 投票数

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def assign_random_avatar(self):
        avatars = [
            'avatars/avatar1.png',
            'avatars/avatar2.png',
            'avatars/avatar3.png',
            'avatars/avatar4.png',
            'avatars/avatar5.png',
            'avatars/avatar6.png',
            'avatars/avatar7.png',
            'avatars/avatar8.png',
            'avatars/avatar9.png',
            'avatars/avatar10.png',
            'avatars/avatar11.png',
            'avatars/avatar12.png',
        ]
        self.avatar = random.choice(avatars)

    def save(self, *args, **kwargs):
        if not self.avatar:
            self.assign_random_avatar()
        super().save(*args, **kwargs)


