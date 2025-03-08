# Generated by Django 5.1.6 on 2025-03-05 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(choices=[('Beer', 'Beer'), ('Wine', 'Wine'), ('category', 'category')], max_length=20, null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]
