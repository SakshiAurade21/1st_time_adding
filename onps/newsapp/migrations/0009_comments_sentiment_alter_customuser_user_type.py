# Generated by Django 5.1.7 on 2025-04-19 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0008_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='sentiment',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(2, 'subadmin'), (1, 'admin')], default=1, max_length=50),
        ),
    ]
