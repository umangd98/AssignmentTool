from django.shortcuts import render
from django.http import JsonResponse, HttpResponseForbidden
import requests


RUN_URL = "https://api.hackerearth.com/code/run/"

# Create your views here.
def index_compiler(request):
  return render(request, 'index_compiler.html', {})


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