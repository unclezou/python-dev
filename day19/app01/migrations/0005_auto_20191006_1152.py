# Generated by Django 2.2.5 on 2019-10-06 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20191006_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergroup',
            name='uptime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_type_id',
            field=models.IntegerField(choices=[(1, '超级用户'), (2, '普通用户'), (3, '普普通用户')], default=1),
        ),
    ]
