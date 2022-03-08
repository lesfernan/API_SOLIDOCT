from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import pkg_resources
from apps.services.models import CategoryService,Service
import json

# Create your views here.
class CategoryServices(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    

    def get (self,request,id=0):
        if (id>0):
            catServices=list(CategoryService.objects.filter(id=id).values())
            if len(catServices)>0:
                catService=catServices[0]
                datos={'message':'Success','ServicesCategory':catService}
            else:
                datos={'message':'Category Services not found...'}
            return JsonResponse(datos)

        else:
            catServices=list(CategoryService.objects.values())
            if len(catServices)>0:
                datos={'message':'Success','ServicesCategories':catServices}
            else:
                datos={'message':'Categories services not found...'}
            return JsonResponse(datos)
            
    def post (self,request):
        jd=json.loads(request.body)
        CategoryService.objects.create(name_service=jd['name_service'])
        datos={'message':'Success'}
        return JsonResponse(datos)
        
    def put (self,request,id):
        jd=json.loads(request.body)
        catServices=list(CategoryService.objects.filter(id=id).values())
        if len(catServices)>0:
            catService=CategoryService.objects.get(id=id)
            catService.name_service=jd['name_service']
            catService.save()
            datos={'message':'Success'}
        else:
            datos={'message':'Companies not found...'}
        return JsonResponse(datos)
        

    def delete (self,request,id):
        catServices=list(CategoryService.objects.filter(id=id).values())
        if len(catServices)>0:
            CategoryService.objects.filter(id=id).delete()
            datos={'message':'Success'}
        else:
            datos={'message':'Companies not found...'}
        return JsonResponse(datos)

class Services(View,CategoryService):
    prueba=CategoryService.objects.get(id=1)
    print(prueba)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get (self,request,id=0):
        if (id>0):
            services=list(Service.objects.filter(id=id).values())
            if len(services)>0:
                service=services[0]
                datos={'message':'Success','ServiceCategory':service}
            else:
                datos={'message':'Services not found...'}
            return JsonResponse(datos)

        else:
            services=list(Service.objects.values())
            if len(services)>0:
                datos={'message':'Success','Services':services}
            else:
                datos={'message':' services not found...'}
            return JsonResponse(datos)
            
    def post (self,request,id=0):
        jd=json.loads(request.body)
        if (id>0):
            Service.objects.get_or_create(name=jd['name'],category=CategoryService(id=id))
            datos={'message':'Success'}
            return JsonResponse(datos)
        else:
            datos={'message':'El id tiene que ser > 0'}
            return JsonResponse(datos)
        # Service.objects.create(name=jd['name'],category_id=jd['category'])
       
    def put (self,request,id):
        jd=json.loads(request.body)
        services=list(Service.objects.filter(id=id).values())
        if len(services)>0:
            service=Service.objects.get(id=id)
            service.name=jd['name']
            service.save()
            datos={'message':'Success'}
        else:
            datos={'message':'services not found...'}
        return JsonResponse(datos)
        
    def delete (self,request,id):
        services=list(Service.objects.filter(id=id).values())
        if len(services)>0:
            Service.objects.filter(id=id).delete()
            datos={'message':'Success'}
        else:
            datos={'message':'service not found...'}
        return JsonResponse(datos)
        
        