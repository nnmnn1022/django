# Generated by Django 4.0.3 on 2022-05-01 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0003_alter_answer_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='status',
            field=models.CharField(choices=[('REG', 'Registe complete'), ('CHE', 'now checking'), ('COM', 'answer complete')], default='REG', max_length=3),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='이미지'),
        ),
    ]
