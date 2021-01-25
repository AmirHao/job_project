from django.db import migrations

from job.models import Role
from utils.auth import md5_


def add_data(apps, _):
    from job.models import User

    queryset = User.objects.all()
    for user in queryset:
        pwd = user.password
        new_pwd = md5_(pwd)
        user.password = new_pwd
        user.save()


class Migration(migrations.Migration):
    dependencies = [
        ('job', '0008_auto_20210115_1144'),
    ]

    operations = [
        migrations.RunPython(add_data),
    ]