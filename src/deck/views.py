from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


from django.shortcuts import redirect

def index(request):
    # return HttpResponse("Under construction.")
    return render(request, "deck.html")