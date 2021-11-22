"""Main URLs module."""

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_simplejwt.views import (TokenRefreshView)

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),

    # path('api/users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/users/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(('bugal.users.urls', 'users'), namespace='users')),
    path('', include(('bugal.contacts.urls', 'contacts'), namespace='contacts')),
    path('', include(('bugal.invoices.urls', 'invoices'), namespace='invoices'))
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
