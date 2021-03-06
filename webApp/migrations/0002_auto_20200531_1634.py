# Generated by Django 3.0.6 on 2020-05-31 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(upload_to='static/image/'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='tag',
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='webApp.tag'),
            preserve_default=False,
        ),
    ]
