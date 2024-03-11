# Generated by Django 5.0.3 on 2024-03-11 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='static/images/')),
                ('date', models.DateTimeField()),
                ('organization', models.ManyToManyField(related_name='organizations', to='organization.organization')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'ordering': ['pk', 'date'],
            },
        ),
    ]
