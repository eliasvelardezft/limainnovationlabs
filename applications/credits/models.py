from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .managers import CreditRequestManager, ClientManager
# Create your models here.


class Client(models.Model):
    
    SENTINEL_RISK_SCORES = (
        (0, 'Bueno'),
        (1, 'Regular'),
        (2, 'Malo'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sbs_debt = models.DecimalField(max_digits=8, decimal_places=2)
    sentinel_risk_score = models.CharField(max_length=10, choices=SENTINEL_RISK_SCORES)

    objects = ClientManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


    
class CreditRequest(models.Model):

    REQUEST_STATUSES = [
        [0, 'Pendiente'],
        [1, 'Rechazada'],
        [2, 'Aceptada'],
    ]

    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    status = models.CharField(max_length=10, choices=REQUEST_STATUSES)
    ai_score = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE)

    objects = CreditRequestManager()

    def __str__(self):
        return f'{self.date} - ${self.amount}\n{self.cliente}'
