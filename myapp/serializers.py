from rest_framework import serializers
from .models import AgeValues, EducationValues, PlaceValues, WeightValues


class AgeValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeValues
        fields = ('id', 'start_age', 'end_age', 'value')


class WeightValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightValues
        fields = ('id', 'start_weight', 'end_weight', 'value')


class EducationValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationValues
        fields = ('id', 'education', 'value')


class PlaceOfBirthValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceValues
        fields = ('id', 'place', 'value')
