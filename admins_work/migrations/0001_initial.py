# Generated by Django 3.2 on 2022-11-23 19:05

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
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=20)),
                ('customer_age', models.IntegerField()),
                ('customer_address', models.CharField(max_length=20)),
                ('customer_mobile', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ExtraServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=20)),
                ('service_price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=20)),
                ('room_status', models.CharField(choices=[('Available', 'Available'), ('NotAvailable', 'NotAvailable')], max_length=20)),
                ('room_type', models.CharField(choices=[('AC', 'AC'), ('NonAC', 'NonAC')], max_length=20)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_mobile', models.CharField(max_length=10)),
                ('user_profile_photo', models.ImageField(default='default.jpg', upload_to='user_images/')),
                ('user_address', models.CharField(max_length=20)),
                ('user_postal_code', models.CharField(max_length=6)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CheckInDate', models.DateField()),
                ('CheckOutDate', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admins_work.customer')),
                ('extra_service', models.ManyToManyField(blank=True, null=True, to='admins_work.ExtraServices')),
                ('rooms', models.ManyToManyField(to='admins_work.Rooms')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
