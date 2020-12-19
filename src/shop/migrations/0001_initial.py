# Generated by Django 2.2 on 2020-12-19 03:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(max_length=150, null=True)),
                ('release_year', models.DateTimeField(null=True)),
                ('shell', models.CharField(max_length=150, null=True)),
                ('mileage', models.IntegerField(null=True)),
                ('transmission', models.CharField(max_length=150, null=True)),
                ('rudder', models.CharField(max_length=60, null=True)),
                ('color', models.CharField(max_length=150, null=True)),
                ('gear', models.CharField(max_length=150, null=True)),
                ('custom_clear', models.CharField(max_length=150, null=True)),
                ('price', models.CharField(max_length=150, null=True)),
                ('engine_volume', models.CharField(max_length=150, null=True)),
                ('city', models.CharField(max_length=250, null=True)),
                ('user_id', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'car',
                'verbose_name_plural': 'cars',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(max_length=300, null=True)),
                ('post_description', models.TextField(null=True)),
                ('views', models.IntegerField(null=True)),
                ('added_to_wishlist', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)])),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('car_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Car')),
                ('user_id', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
            },
        ),
    ]
