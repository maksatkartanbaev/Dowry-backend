from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from .models import AgeValues, EducationValues, PlaceValues, WeightValues


class DowryView(APIView):
    @staticmethod
    def post(request):
        age = request.data.get('age')
        age_weight = AgeValues.objects.get(start_age__lte=age, end_age__gte=age)
        weight = request.data.get('weight')
        weight_weight = WeightValues.objects.get(start_weight__lte=weight, end_weight__gte=weight)
        education_weight = EducationValues.objects.get(education=request.data['education'])
        place_of_birth_weight = PlaceValues.objects.get(place=request.data['place_of_birth'])

        price = place_of_birth_weight.value * age_weight.value * weight_weight.value * education_weight.value

        return Response({'price': price})


class EducationList(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        educations = EducationValues.objects.all()
        data = {'educations': [{"name": education.education} for education in educations]}
        return JsonResponse(data, safe=False)


class PlaceList(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        places = PlaceValues.objects.all()
        data = {'places': [{"name": place.place} for place in places]}
        return JsonResponse(data, safe=False)
