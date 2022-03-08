from django.urls import path
from apps.employees.views import Employees 

urlpatterns = [
    path('employees',Employees.as_view(),name='services-categories'),
    path('employees/<int:id>',Employees.as_view(),name='employees_filter'),
    path('employees/<int:id>/<int:id_document>/<int:id_position>',Employees.as_view(),name='employees_new'),
    # path('services',Services.as_view(),name='services'),
    # path('services/<int:id>',Services.as_view(),name='service'),
]