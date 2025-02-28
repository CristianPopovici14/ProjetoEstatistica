from django.urls import path
from .views import survey, results, to_survey

urlpatterns = [
    path('survey/', survey, name='survey'),
    path('results/', results, name='results'),
    path('export/', to_survey, name='to_survey')
]