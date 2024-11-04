# Generated by Django 5.1.2 on 2024-11-02 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название новости')),
                ('short_description', models.CharField(max_length=200, verbose_name='Краткое описание новости')),
                ('text', models.TextField(verbose_name='Новость')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
                ('author', models.CharField(max_length=50, verbose_name='Имя пользователя')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
