# Generated by Django 3.2.5 on 2022-05-05 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0044_alter_portfolioitem_name_alter_serviceoffering_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="source",
            name="last_refresh_stats",
            field=models.JSONField(
                blank=True,
                default={},
                help_text="The result stats for the last source refresh",
            ),
        ),
    ]
