# Generated by Django 3.0.5 on 2020-04-16 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200417_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopitems',
            name='offer_percent',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
    ]