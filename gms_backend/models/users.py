from djongo import models

from gms_backend.models.abstract_date_time import AbstractDateTime


class User(AbstractDateTime):
    name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=15)
    age = models.IntegerField()
    dob = models.DateField(null=True,blank=True)


    class Meta:
        managed=True
    
    def __str__(self) -> str:
        return self.name