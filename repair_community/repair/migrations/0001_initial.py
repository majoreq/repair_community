# Generated by Django 2.1.1 on 2018-09-12 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(max_length=128, verbose_name='device')),
                ('description', models.TextField(verbose_name='description')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('assigned_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_to', to=settings.AUTH_USER_MODEL, verbose_name='assigned to')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
        ),
    ]
