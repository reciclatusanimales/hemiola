# Generated by Django 2.2 on 2021-01-05 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_item_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2020-12-31 06:01:00.018279-05'),
            preserve_default=False,
        ),
    ]
