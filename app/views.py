from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *


# Returning string as response by using Function Based View

def fbv_string(request):
    return HttpResponse('<h1>A message from Function Based View_string')

# Returning string as response by using Class Based View

class cbv_string(View):
    def get(self,request):
        return HttpResponse('<h1>A message from Class Based View_string')
    
# Rendering html by FBV
    
def fbv_html(request):
    return render(request,'fbv_html.html')

# Rendering html by CBV

class cbv_html(View):
    def get(self,request):
        return render(request,'cbv_html.html')

# Insert data by FBV through Models Forms
    
def insert_school_by_fbv(request):
    EFDO=SchoolForm()
    d={'EFDO':EFDO}
    if request.method=='POST':
        SDFO=SchoolForm(request.POST)
        if SDFO.is_valid():
            SDFO.save()
            return HttpResponse('insert_school_by_fbv is Done')
    return render(request,'insert_school_by_fbv.html',d)

# Insert data by CBV

class InsertSchoolByCbv(View):
    def get(self,request):
        ESFO=SchoolForm()
        d={'ESFO':ESFO}
        return render(request,'InsertSchoolByCbv.html',d)
    
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('InsertSchoolByCbv is done')

# Rendering html page by using TemplateView
        
class Cbv_Template(TemplateView):
    template_name='Cbv_Template.html'