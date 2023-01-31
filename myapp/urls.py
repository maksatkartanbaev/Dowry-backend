from django.urls import path
from .views import DowryView, EducationList, PlaceList

urlpatterns = [
    path('dowry/', DowryView.as_view(), name='dowry'),
    path('education/', EducationList.as_view(), name='education-list'),
    path('places/', PlaceList.as_view(), name='place-list'),
]
