# Generated by Django 4.2 on 2023-05-04 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_purpose_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='checkbox',
            field=models.CharField(default='empty', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='form',
            name='phone',
            field=models.IntegerField(),
        ),
    ]