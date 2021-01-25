from django.db import migrations


def add_data(apps, _):
    from job.models import Role

    role_list = ['求职者', '招聘者', '管理员']
    for i in role_list:
        res = Role.objects.create(name=f'{i}')


class Migration(migrations.Migration):
    dependencies = [
        ('job', '0003_auto_20210111_1540'),
    ]

    operations = [
        migrations.RunPython(add_data),
    ]
