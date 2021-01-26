from django.contrib import admin

# Register your models here.
# import os
#
# from django.conf import settings
#
# list_dirs = os.walk(settings.BASE_DIR + '/blue/admins/')
# test_vars = vars()
#
# for root, dirs, files in list_dirs:
#     for file in files:
#         if file == '__init__.py':
#             continue
#         if not file.endswith('.py'):
#             continue
#         # 找到 blue/testscases/ 下面的 py 文件
#         from_name = file.replace('.py', '')
#         import_result = __import__('blue.admins.' + from_name, globals(), locals(), [from_name], 0)
from job import models
from job.models.user_limit import UserLimit

admin.site.register(models.company.Company)
# class CompanyAdmin(admin.ModelAdmin):
#     list_display = ['user', 'name', 'mobile', 'email', 'registration_at', 'employees_num', 'address', 'company_profile'] # 需要展示的字段


@admin.register(UserLimit)
class UserLimitAdmin(admin.ModelAdmin):
    list_display = ('user__name', 'user__role', 'is_enable')
    fields = ('user',)
    search_fields = ('user__name', 'user__email')
    actions = ['delete', 'update', ]
    list_per_page = 10
    list_filter = ('user__name', 'user__role')
    list_editable = ('is_enable',)

    def user__name(self, obj):
        return obj.user.name

    def user__role(self, obj):
        return obj.user.role.name

    user__name.short_description = '用户名称'
    user__role.short_description = '角色名称'
