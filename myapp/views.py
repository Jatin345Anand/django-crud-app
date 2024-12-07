from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello, Django!")

from django.shortcuts import render
from django.http import JsonResponse

counter_value = {"count": 0}

# def home(request):
#     return render(request, 'index.html')
def index(request):
    return render(request, 'index.html')

def increment_counter(request):
    global counter_value
    if request.method == "POST":
        counter_value["count"] += 1
    return JsonResponse(counter_value)

