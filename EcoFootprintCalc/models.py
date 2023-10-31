from django.db import models


class VehicleType(models.Model):
    name = models.CharField(max_length=255)
    note = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Type de véhicule"


class Energy(models.Model):
    name = models.CharField(max_length=255)
    note = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Énergie"


class Kilometers(models.Model):
    start = models.IntegerField()
    end = models.IntegerField()
    note = models.IntegerField()

    def __str__(self):
        return f"{self.start}-{self.end}"

    class Meta:
        verbose_name = "Kilométrage"


class Years(models.Model):
    start = models.IntegerField()
    end = models.IntegerField()
    note = models.IntegerField()

    def __str__(self):
        return f"{self.start}-{self.end}"

    class Meta:
        verbose_name = "Années"


class InterestRate(models.Model):
    start = models.FloatField()
    end = models.FloatField()
    percentage = models.FloatField()

    def __str__(self):
        return f"{self.start}-{self.end}"

    class Meta:
        verbose_name = "Taux d'intérêt"


class Passengers(models.Model):
    number = models.IntegerField()
    percentage = models.FloatField()

    def __str__(self):
        return f"{self.number}"

    class Meta:
        verbose_name = "Passagers"
