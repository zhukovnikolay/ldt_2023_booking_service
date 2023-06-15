# Generated by Django 4.1.8 on 2023-05-27 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("halls", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hall",
            name="moderated",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="halls.hallmoderatingstatus",
            ),
        ),
    ]