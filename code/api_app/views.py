from django.shortcuts import render
from django.http import HttpResponse
import subprocess

def home(request):
    return render(request, 'api_app/home.html')

def execute_script(request):
    if request.method == 'POST':
        # Execute your Python script here
        script_output = subprocess.check_output(['python3', 'src/sids.py'])
        return render(request, 'api_app/results.html', {'output': script_output})
    else:
        return HttpResponse('Invalid request method.')

def execute_script2(request):
    if request.method == 'POST':
        # Execute your Python script here
        script_output2 = subprocess.check_output(['python3', 'src/stars.py'])
        return render(request, 'api_app/results.html', {'output': script_output2})
    else:
        return HttpResponse('Invalid request method.')