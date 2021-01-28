# Generated by Django 3.1.4 on 2021-01-12 08:21

from django.db import migrations, models
import django.db.models.deletion
import job.models.helper.enums


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_add_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modify_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=32, verbose_name='岗位名称')),
                ('work_address', models.CharField(max_length=128, verbose_name='工作地址')),
                ('hiring_num', models.PositiveIntegerField(default=0, verbose_name='招聘人数')),
                ('salary', models.CharField(max_length=32, null=True, verbose_name='薪水')),
                ('Job_description', models.CharField(default='', max_length=256, verbose_name='岗位介绍')),
                ('professional', models.CharField(max_length=20, null=True, verbose_name='专业要求')),
                ('education', models.CharField(max_length=20, null=True, verbose_name='学历要求')),
                ('work_experience', models.CharField(default='', max_length=20, verbose_name='工作经验')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
                ('contacter', models.CharField(max_length=20, verbose_name='联系人')),
                ('mobile', models.CharField(max_length=11, verbose_name='联系电话')),
                ('email', models.EmailField(max_length=128, null=True, verbose_name='邮箱')),
                ('cerate_person', models.CharField(default='', max_length=20, verbose_name='创建人')),
                ('change_person', models.CharField(default='', max_length=20, verbose_name='修改人')),
                ('company', models.ForeignKey(db_column='company_id', on_delete=django.db.models.deletion.CASCADE, related_name='job', to='job.company', verbose_name='企业')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(help_text='手机号不能重复', max_length=11, unique=True, verbose_name='手机号'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=20, verbose_name='姓名'),
        ),
        migrations.CreateModel(
            name='Job2Jianli',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modify_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('status', models.IntegerField(choices=[(1, '待查看'), (2, '已查看'), (3, '通过'), (4, '驳回')], default=job.models.helper.enums.job2jianliEnum['to_view'], verbose_name='状态')),
                ('jianli', models.ForeignKey(db_column='jianli_id', on_delete=django.db.models.deletion.CASCADE, related_name='job2jianli', to='job.jianli', verbose_name='简历')),
                ('job', models.ForeignKey(db_column='job_id', on_delete=django.db.models.deletion.CASCADE, related_name='job2jianli', to='job.job', verbose_name='岗位')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]