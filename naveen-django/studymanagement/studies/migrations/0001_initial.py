# Generated by Django 5.1.2 on 2024-10-11 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_name', models.CharField(max_length=50)),
                ('study_phase', models.CharField(choices=[('phase I', 'phase I'), ('phase II', 'phase II'), ('phase III', 'phase III'), ('phase IV', 'phase IV')], max_length=50)),
                ('sponsor_name', models.CharField(max_length=60)),
                ('study_description', models.TextField()),
            ],
        ),
    ]
