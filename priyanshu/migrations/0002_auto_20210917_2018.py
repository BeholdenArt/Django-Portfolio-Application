# Generated by Django 3.2.7 on 2021-09-17 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('priyanshu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='profile_img',
            field=models.ImageField(upload_to='ProfileImg/'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(upload_to='PortfolioImg/'),
        ),
    ]