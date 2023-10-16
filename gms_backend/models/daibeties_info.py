from djongo import models

from gms_backend.models.abstract_date_time import AbstractDateTime


class DiabetiesType:
    TYPE1 = "TYPE 1"
    TYPE2 = "TYPE 2"

    CHOICES = ((TYPE1, TYPE1), (TYPE2, TYPE2))


class DiabetiesInfo(AbstractDateTime):
    user = models.ForeignKey("gms_backend.User", on_delete=models.PROTECT)
    type = models.CharField(choices=DiabetiesType.CHOICES, max_length=20)
    notes = models.JSONField(default = {})

    class Meta:
        managed = True
