# Generated by Django 5.1.1 on 2024-10-02 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data_loader", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="produto",
            name="stock",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
