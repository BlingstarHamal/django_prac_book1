# Generated by Django 4.2.8 on 2023-12-27 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_hashtag_post_tags'),
        ('users', '0002_user_profile_image_user_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='like_posts',
            field=models.ManyToManyField(blank=True, related_name='like_users', to='posts.post', verbose_name='좋아요 누른 Post 목록'),
        ),
    ]
