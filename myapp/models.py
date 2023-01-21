from django.db import models


class AgeValues(models.Model):
    start_age = models.IntegerField()
    end_age = models.IntegerField()
    value = models.FloatField()


class WeightValues(models.Model):
    start_weight = models.IntegerField()
    end_weight = models.IntegerField()
    value = models.FloatField()


class EducationValues(models.Model):
    education = models.CharField(max_length=100)
    value = models.FloatField()


class PlaceValues(models.Model):
    place = models.CharField(max_length=100)
    value = models.FloatField()
