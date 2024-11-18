from django.contrib import admin
from .models import Poll, Choice
from django.contrib.auth.models import User
from .models import UserProfile

# 自定义 PollAdmin
class PollAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'end_date')  # 显示 title、created_by 和 end_date
    list_filter = ('created_by', 'end_date')  # 添加筛选器
    search_fields = ('title', 'created_by__username')  # 添加搜索功能

# 自定义 ChoiceAdmin
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'poll__title', 'poll__created_by')  # 显示 choice_text 和关联的 poll
    list_filter = ('poll__title',)  # 按照 poll 进行筛选
    search_fields = ('choice_text',)  # 添加搜索功能

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'

class UserAdmin(admin.ModelAdmin):
    inlines = (UserProfileInline,)


# 注册模型和自定义的 ModelAdmin
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
