# Generated by Django 4.2 on 2024-05-08 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_comment_like_users_alter_article_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='v1iew_count',
            field=models.IntegerField(default=0),
        ),
    ]