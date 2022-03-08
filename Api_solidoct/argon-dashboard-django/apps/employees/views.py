from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import pkg_resources
from apps.employees.models import Gender,DocumentType,Employee, Position

import json

# Create your views here.
class Employees(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    

    def get (self,request,id=0):
        if (id>0):
            catServices=list(Employee.objects.filter(id=id).values('id','date_birth','cell','gender'))
            if len(catServices)>0:
                catService=catServices[0]
                datos={'message':'Success','ServicesCategory':catService}
                # datos = {"results": list(gender.values('id', 'long_name', 'short_name'))}
                return JsonResponse(datos)

            else:
                datos={'message':'Category Services not found...'}
            return JsonResponse(datos)

        else:
            catServices=list(Employee.objects.values())
            if len(catServices)>0:
                datos={'message':'Success','ServicesCategories':catServices}
            else:
                datos={'message':'Categories services not found...'}
            return JsonResponse(datos)
            
    def post (self,request,id=1,id_document=1,id_position=1):
        jd=json.loads(request.body)
        if (id>0):
            Employee.objects.get_or_create(name=jd['name'],last_name=jd['last_name'],gender=id,document_type_id=id_document,position=Position(id=id_position),date_birth=jd['date_birth'],cell=jd['cell'],img=jd['img'])
            datos={'message':'Success'}
            return JsonResponse(datos)
        else:
            datos={'message':'Los IDs tiene que ser > 0'}
            return JsonResponse(datos)
        # Service.objects.create(name=jd['name'],category_id=jd['category'])
        
    def put (self,request,id):
        jd=json.loads(request.body)
        catServices=list(Employee.objects.filter(id=id).values())
        if len(catServices)>0:
            catService=Employee.objects.get(id=id)
            catService.name_service=jd['name_service']
            catService.save()
            datos={'message':'Success'}
        else:
            datos={'message':'Companies not found...'}
        return JsonResponse(datos)
        