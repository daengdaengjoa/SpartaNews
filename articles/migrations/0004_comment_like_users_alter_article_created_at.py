# Generated by Django 4.2 on 2024-05-08 00:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0003_merge_20240507_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='like_users',
            field=models.ManyToManyField(related_name='like_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]