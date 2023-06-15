# Generated by Django 4.1.8 on 2023-05-27 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("halls", "0006_alter_hall_address_alter_hall_area_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hall",
            name="moderated",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="halls.hallmoderatingstatus",
            ),
        ),
    ]
