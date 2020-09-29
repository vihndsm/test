# Generated by Django 3.1.1 on 2020-09-28 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price2',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products'),
        ),
    ]
