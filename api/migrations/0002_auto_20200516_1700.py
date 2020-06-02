# Generated by Django 3.0.4 on 2020-05-16 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': '作者', 'verbose_name_plural': '作者'},
        ),
        migrations.AlterModelOptions(
            name='authordetail',
            options={'verbose_name': '作者详情', 'verbose_name_plural': '作者详情'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '书籍', 'verbose_name_plural': '书籍'},
        ),
        migrations.AlterModelOptions(
            name='publish',
            options={'verbose_name': '出版社', 'verbose_name_plural': '出版社'},
        ),
        migrations.AlterModelTable(
            name='author',
            table='old_boy_author',
        ),
        migrations.AlterModelTable(
            name='authordetail',
            table='old_boy_author_detial',
        ),
        migrations.AlterModelTable(
            name='book',
            table='old_boy_book',
        ),
        migrations.AlterModelTable(
            name='publish',
            table='old_boy_publish',
        ),
    ]
