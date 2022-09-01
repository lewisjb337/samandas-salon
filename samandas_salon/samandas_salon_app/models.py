from django.db import models

class service(models.Model):
    service_name = models.CharField(max_length=50)
    service_description = models.CharField(max_length=5000)
    service_price = models.CharField(max_length=30)
    service_category = models.CharField(max_length=50)

    def __str__(self):
        return self.service_name
