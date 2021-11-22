from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.invoices import InvoiceViewSet

app_name = 'invoices'

router = DefaultRouter()

router.register(r'invoices', InvoiceViewSet, basename='invoices')

urlpatterns = [
    path('api/v1/', include(router.urls))
]
