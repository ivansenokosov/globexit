# Generated by Django 4.2.3 on 2024-05-28 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GlobexUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=100, verbose_name='Имейл')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('position_name', models.CharField(max_length=100, verbose_name='Должность')),
                ('department', models.CharField(max_length=100, verbose_name='Департамент')),
                ('hire_date', models.DateField(max_length=100, verbose_name='Дата найма')),
            ],
            options={
                'verbose_name': 'Пользователи',
                'verbose_name_plural': 'Пользователь',
                'db_table': 'd_globexit_users',
            },
        ),
    ]