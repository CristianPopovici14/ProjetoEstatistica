from django.shortcuts import render, redirect
from .forms import UploadSurvey
from .models import Data
from django.http import HttpResponse
import csv

def survey(request):
    if request.POST:
        form = UploadSurvey(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'survey.html', {'form': UploadSurvey})

def results(request):
    responses = Data.objects.all()
    return render(request, 'results.html', {'responses': responses})

def to_survey(request):
    responses = Data.objects.all().values_list('socialtime', 'sleeptime')
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['socialtime', 'sleeptime'])

    for survey_response in responses:
        writer.writerow(survey_response)

    response['Content-Disposition'] = 'attachment file; filename="responses.csv"'
    return response