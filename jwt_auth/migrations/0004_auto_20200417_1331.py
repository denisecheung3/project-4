# Generated by Django 3.0.5 on 2020-04-17 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_auth', '0003_auto_20200417_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]