# Generated by Django 4.0.4 on 2022-05-28 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_opportunity_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
