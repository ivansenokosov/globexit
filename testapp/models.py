from django.db import models

class GlobexUsers(models.Model):
    name = models.CharField(max_length=100, blank=False, null = False, verbose_name='Имя')
    phone = models.CharField(max_length=100, blank=False, null = False, verbose_name='Телефон')
    email = models.EmailField(max_length=100, blank=False, null = False, verbose_name='Имейл')
    address = models.CharField(max_length=100, blank=False, null = False, verbose_name='Адрес')
    position_name = models.CharField(max_length=100, blank=False, null = False, verbose_name='Должность')
    department = models.CharField(max_length=100, blank=False, null = False, verbose_name='Департамент')
    hire_date = models.DateField(max_length=100, blank=False, null = False, verbose_name='Дата найма')

    class Meta:
        db_table = 'd_globexit_users'
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователь"

    def __str__(self):
        return f'{self.name}'
