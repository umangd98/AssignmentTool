from django.shortcuts import render
from django.http import JsonResponse, HttpResponseForbidden
import requests
from Assignments.models import Assignment
from Submission.models import Submission
import urllib
import json


RUN_URL = "https://api.hackerearth.com/code/run/"

# Create your views here.
def index_compiler(request):
  group = request.user.groups.all()[0].name
  is_instructor = False
  if group == 'instructor':
    #send form
    is_instructor=True

  return render(request, 'index_compiler.html', {'is_instructor': is_instructor})


def run_compiler(request):
  if request.is_ajax():
    source = request.POST['source']
    lang = request.POST['lang']
    data = {
      'client_secret': '6dbba821a6571d9342957d49af2d2e0602396f38' ,
      'async': 0,
      'source': source,
      'lang': lang,
      'time_limit': 5,
      'memory_limit': 262144,
    }
    if 'input' in request.POST:
      data['input'] = request.POST['input']
      print('input : ',data['input'])
    
    r = requests.post(RUN_URL, data=data)
    print('result : ',r.json())
    return JsonResponse(r.json(), safe=False)
  else:
	  return HttpResponseForbidden()


def run_check(request):
  if request.is_ajax():
    assignment_id = request.POST['assignment_id']
    submission_id = request.POST['submission_id']
    assignment = Assignment.objects.get(id=assignment_id)
    submission = Submission.objects.get(id=submission_id)
    url_submission = submission.submission_file.url
    f = requests.get(url_submission)
    source_code = f.text
    input_cases_url = assignment.input_test_cases.url
    f = requests.get(input_cases_url)
    input_cases = f.text
    # print(file)
    # print('ajax', assignment, submission)
    request_data = {
      'client_secret': '6dbba821a6571d9342957d49af2d2e0602396f38' ,
      'async': 0,
      'source': source_code,
      'lang': "C",
      'time_limit': 5,
      'memory_limit': 262144,
    }
    if input_cases:
      request_data['input'] = input_cases

    r = requests.post(RUN_URL, data=request_data)
    print('result : ',r.json())

    output_cases_url = assignment.output_test_cases.url
    f = requests.get(output_cases_url)
    output_cases = f.text

    output = r.json()['run_status']['output']

    # print('output_cases ', output_cases)
    # print('output ', output)

    time_used = r.json()['run_status']['time_used']
    memory_used = r.json()['run_status']['memory_used']
    ret = 'Output didn\'t matched Correctly!'




    output_lines = output.splitlines()
    output_cases_lines = output_cases.splitlines()
    
    output_lines = [item.strip() for item in output_lines]
    output_cases_lines = [item.strip() for item in output_cases_lines]


    # print('output_cases ', output_cases_lines)
    # print('output ', output_lines)
    
    if output_cases_lines == output_lines:
      ret = 'Compiler Message: Output matched Correctly!'
      print('matched')

        
    res_data = {
      'text': ret,
      'time_used': time_used, 
      'memory_used': memory_used,
      "output_cases_lines": output_cases_lines,
      "input_cases": input_cases,
      "output_lines": output_lines      
    }
    return JsonResponse(res_data, safe=False)
