from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AgeValues, EducationValues, PlaceValues, WeightValues


class DowryView(APIView):
    def post(self, request):
        age = request.data.get('age')
        age_weight = AgeValues.objects.get(start_age__lte=age, end_age__gte=age)
        weight = request.data.get('weight')
        weight_weight = WeightValues.objects.get(start_weight__lte=weight, end_weight__gte=weight)
        education_weight = EducationValues.objects.get(education=request.data['education'])
        place_of_birth_weight = PlaceValues.objects.get(place=request.data['place_of_birth'])

        price = place_of_birth_weight.value * age_weight.value * weight_weight.value * education_weight.value

        return Response({'price': price})
