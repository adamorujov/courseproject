from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from account.api.serializers import AccountSerializer, RegisterSerializer
from account.api.permissions import IsOwn
from account.models import Account

class AccountListAPIView(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountRetrieveAPIView(RetrieveAPIView):
    lookup_field = "email"
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated, IsOwn) 

class RegisterAPIView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (IsAdminUser,)
