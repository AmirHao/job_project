from django.db import migrations

from job.models import Role


def add_data(apps, _):
    from job.models import User

    user_list = [
        {'name': '唐三', 'mobile': '13212345673', 'password': '13212345673', 'email': '13212345673@qq.com', 'role': 3},
        {'name': '唐四', 'mobile': '13212345674', 'password': '13212345674', 'email': '13212345674@qq.com', 'role': 4},
        {'name': '唐五', 'mobile': '13212345675', 'password': '13212345675', 'email': '13212345675@qq.com', 'role': 1},
        {'name': '唐六', 'mobile': '13212345676', 'password': '13212345676', 'email': '13212345676@qq.com', 'role': 2},
        {'name': '唐七', 'mobile': '13212345677', 'password': '13212345677', 'email': '13212345677@qq.com', 'role': 3},
        {'name': '唐八', 'mobile': '13212345678', 'password': '13212345678', 'email': '13212345678@qq.com', 'role': 4},
        {'name': '唐九', 'mobile': '13212345679', 'password': '13212345679', 'email': '13212345679@qq.com', 'role': 1},
        {'name': '唐十', 'mobile': '13212345610', 'password': '13212345610', 'email': '13212345610@qq.com', 'role': 2},
        {'name': '唐十一', 'mobile': '13212345611', 'password': '13212345611', 'email': '13212345611@qq.com', 'role': 3},
        {'name': '唐十二', 'mobile': '13212345612', 'password': '13212345612', 'email': '13212345612@qq.com', 'role': 4},
        {'name': '唐十三', 'mobile': '13212345613', 'password': '13212345613', 'email': '13212345613@qq.com', 'role': 1},
        {'name': '唐十四', 'mobile': '13212345614', 'password': '13212345614', 'email': '13212345614@qq.com', 'role': 2},
        {'name': '唐十五', 'mobile': '13212345615', 'password': '13212345615', 'email': '13212345615@qq.com', 'role': 3},
    ]
    queryset = Role.objects.all()
    role_dict = {}
    for role in queryset:
        role_dict[f'{role.id}'] = role
    for user in user_list:
        id = user.pop('role')
        user['role'] = role_dict[f'{id}']
        res = User.objects.create(**user)


class Migration(migrations.Migration):
    dependencies = [
        ('job', '0006_auto_20210112_1706'),
    ]

    operations = [
        migrations.RunPython(add_data),
    ]