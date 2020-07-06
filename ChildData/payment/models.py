from django.conf import settings
from django.db import models

from fielddata.models import Child_Entry

User=settings.AUTH_USER_MODEL

class Adoption(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    Child_id = models.DecimalField(max_digits=10, decimal_places=0)
    Child_name = models.CharField(max_length=32)
    Gender = models.CharField(max_length=32)
    total = models.DecimalField(default=0.00, max_digits=10,decimal_places=2)
    link = models.CharField(max_length=100)
    timestrmp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)