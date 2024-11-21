# Generated by Django 2.1 on 2018-08-22 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_bank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bank',
            name='Names',
        ),
        migrations.AddField(
            model_name='user',
            name='CVV',
            field=models.CharField(default='', max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='Card_Number',
            field=models.CharField(default='', max_length=16),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Bank',
        ),
    ]
