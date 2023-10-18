from django.db import models

# Create your models here.

class Advertisiment(models.Model):
    title = models.CharField('Заголок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auctions = models.BooleanField('Торг', help_text='Укажите, уместен ли торг')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'advertisements'