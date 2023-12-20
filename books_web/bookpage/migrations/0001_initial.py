# Generated by Django 4.2.6 on 2023-12-16 04:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homepage', '0002_masterbooks_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=1000)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.masterbooks')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]