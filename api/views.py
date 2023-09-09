from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from datetime import datetime

def home(request):
    return HttpResponse('"status_code": 200')

def get_info(request):
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    if slack_name is None or track is None:
        return JsonResponse({'error': 'Please provide both the slack_name and track parameters.'})

    # Get the current date and time
    current_time = datetime.utcnow()
    current_day = current_time.strftime("%A")  # Get the current day as a string
    utc_time = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")  # Get the current UTC time in the desired format

    info = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": "https://github.com/GodswillEdet/Task1/blob/main/api/views.py",
        "github_repo_url": "https://github.com/GodswillEdet/Task1",
        "status_code": 200
    }
    return JsonResponse(info)



