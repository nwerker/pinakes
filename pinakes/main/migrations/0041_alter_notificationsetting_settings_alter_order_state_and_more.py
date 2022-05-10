# Generated by Django 4.0.2 on 2022-04-18 18:10

from django.db import migrations, models
import pinakes.main.approval.models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0040_seed_email_notification_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notificationsetting",
            name="settings",
            field=pinakes.main.approval.models.SettingField(
                blank=True,
                help_text="Parameters for configuring the notification method",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="state",
            field=models.CharField(
                choices=[
                    ("Approval Pending", "Pending"),
                    ("Approved", "Approved"),
                    ("Canceled", "Canceled"),
                    ("Completed", "Completed"),
                    ("Created", "Created"),
                    ("Denied", "Denied"),
                    ("Failed", "Failed"),
                    ("Ordered", "Ordered"),
                ],
                default="Created",
                editable=False,
                help_text="Current state of the order",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="state",
            field=models.CharField(
                choices=[
                    ("Approval Pending", "Pending"),
                    ("Approved", "Approved"),
                    ("Canceled", "Canceled"),
                    ("Completed", "Completed"),
                    ("Created", "Created"),
                    ("Denied", "Denied"),
                    ("Failed", "Failed"),
                    ("Ordered", "Ordered"),
                ],
                default="Created",
                editable=False,
                help_text="Current state of this order item",
                max_length=10,
            ),
        ),
    ]
