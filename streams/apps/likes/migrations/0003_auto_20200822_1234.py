# Generated by Django 3.0.5 on 2020-08-22 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20200822_1234'),
        ('likes', '0002_auto_20200816_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comments.PostComment'),
        ),
    ]
