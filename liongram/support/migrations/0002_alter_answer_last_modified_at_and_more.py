# Generated by Django 4.0.3 on 2022-05-01 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='last_modified_at',
            field=models.DateTimeField(auto_now=True, verbose_name='수정일시'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='last_modified_at',
            field=models.DateTimeField(auto_now=True, verbose_name='수정일시'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='last_modified_at',
            field=models.DateTimeField(auto_now=True, verbose_name='수정일시'),
        ),
    ]
