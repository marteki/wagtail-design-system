# Generated by Django 2.2.1 on 2019-05-15 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='componentpage',
            name='status',
            field=models.CharField(choices=[('proposed', 'Proposed'), ('in_progress', 'In progress'), ('beta', 'Beta'), ('released', 'Released')], default='proposed', max_length=32),
        ),
    ]
