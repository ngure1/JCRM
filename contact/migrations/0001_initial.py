# Generated by Django 5.1.6 on 2025-02-20 08:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('category', models.CharField(choices=[('general', 'General Inquiry'), ('prayer', 'Prayer Request'), ('support', 'Technical Support'), ('other', 'Other')], default='general', max_length=20)),
                ('message', models.TextField()),
                ('sent_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
    ]
