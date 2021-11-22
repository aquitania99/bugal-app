"""User URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import users as user_views
from .views import bank_accounts as bank_account_views
from .views import businesses as business_views
from .views import shifts as shift_views
from .views import rates as rate_views
from .views import payment_methods as payment_method_views
from .views import expense_categories as expense_category_views
from .views import expenses as expense_views

router = DefaultRouter()

router.register(r'users', user_views.UserViewSet, basename='user')
router.register(r'shifts/type', shift_views.ShiftTypeViewSet, basename='shift-type')
router.register(r'shifts', shift_views.ShiftInfoViewSet, basename='shift')
# router.register(r'bank_accounts', bank_account_views.BankAccountViewSet, basename='bank')
# router.register(r'businesses', business_views.BusinessInfoViewSet, basename='business')
router.register(r'rates', rate_views.RateViewSet, basename='rate')
router.register(r'payment_methods', payment_method_views.PaymentMethodViewSet, basename='payment-method')
router.register(r'expense_categories', expense_category_views.ExpenseCategoryViewSet, basename='expense-category')
router.register(r'expenses', expense_views.ExpenseViewSet, basename='expense')

urlpatterns = [
    path('api/v1/users/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/v1/', include(router.urls)),
]
