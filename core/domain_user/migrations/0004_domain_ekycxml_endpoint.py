# Generated by Django 3.2.8 on 2021-10-30 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain_user', '0003_auto_20211030_0337'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='ekycxml_endpoint',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
