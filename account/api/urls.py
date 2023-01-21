from django.urls import path
from account.api import views

urlpatterns = [
    path('accounts/', views.AccountListAPIView.as_view(), name="accounts"),
    path('register/', views.RegisterAPIView.as_view(), name="register"),
    path('account/<email>/', views.AccountRetrieveAPIView.as_view(), name="account"),
]
