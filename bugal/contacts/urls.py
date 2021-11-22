"""Contact URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import contacts as contact_views

router = DefaultRouter()

# router.register(r'guardians', guardian_views.GuardianInfoViewSet, basename='guardian')
router.register(r'contacts', contact_views.ContactViewSet, basename='contact')

urlpatterns = [path('api/v1/', include(router.urls)), ]

