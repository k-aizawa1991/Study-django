from django.db import models


class EnergyLog(models.Model):
    """電力ログ"""
    date = models.DateField(verbose_name='日付')
    generation_amount = models.DecimalField(
        verbose_name='発電量',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True)

# Create your models here.
