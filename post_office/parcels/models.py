from django.db import models


class Parcels(models.Model):
    senders_name = models.CharField(max_length=128)
    receiver_name = models.CharField(max_length=128)
    point_of_departure = models.TextField()
    pick_up_piont = models.TextField()
    sender_index = models.IntegerField()
    recipient_index = models.IntegerField()
    phone_number = models.CharField(max_length=10)
    pay_sum = models.IntegerField(null=True, blank=True)
    parcel_type = models.ForeignKey('ParcelsCategory', on_delete=models.PROTECT, null=True)
    

    def __str__(self):
        return self.senders_name
    
class ParcelsCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
