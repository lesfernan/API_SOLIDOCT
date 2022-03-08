from django.urls import path
from apps.services.views import CategoryServices,Services

urlpatterns = [
    path('services/categories',CategoryServices.as_view(),name='services-categories'),
    path('services/categories/<int:id>',CategoryServices.as_view(),name='service-category'),
    path('services',Services.as_view(),name='services'),
    path('services/<int:id>',Services.as_view(),name='service'),
]