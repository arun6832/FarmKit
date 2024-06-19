# Generated by Django 4.2.7 on 2024-03-21 05:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Farm', '0004_alter_cartitem_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='order',
            field=models.ForeignKey(default=django.utils.timezone.now, null=True, on_delete=django.db.models.deletion.CASCADE, to='Farm.farmerorder'),
        ),
    ]