from django.urls import path
from .views import DowryView

urlpatterns = [
    path('dowry/', DowryView.as_view(), name='dowry'),
]
