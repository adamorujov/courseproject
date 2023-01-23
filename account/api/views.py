from rest_framework.views import APIView
from rest_framework.generics import (ListAPIView, 
CreateAPIView, 
RetrieveAPIView,
UpdateAPIView,
get_object_or_404
)

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from account.api.serializers import (AccountSerializer, 
RegisterSerializer, 
CourseListSerializer, 
CourseCreateUpdateSerializer,
UnitCreateUpdateSerializer
)

from account.api.permissions import IsOwner
from account.models import Account, Course, Unit

class AccountListAPIView(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountRetrieveAPIView(RetrieveAPIView):
    lookup_field = "email"
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated, IsOwner) 

class RegisterAPIView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (IsAdminUser,)

class CourseListAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer

class AccountCoursesListAPIView(ListAPIView):
    def get_queryset(self):
        return Course.objects.filter(accounts=self.request.user)
    serializer_class = CourseListSerializer
    permission_classes = (IsAuthenticated, )

class CourseCreateAPIView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCreateUpdateSerializer
    permission_classes = (IsAdminUser,)

class CourseUpdateAPIView(UpdateAPIView):
    lookup_field = "pk"
    queryset = Course.objects.all()
    serializer_class = CourseCreateUpdateSerializer
    permission_classes = (IsAdminUser,)

class UnitCreateAPIView(CreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitCreateUpdateSerializer

class UnitUpdateAPIView(UpdateAPIView):
    lookup_field = "pk"
    queryset = Unit.objects.all()
    serializer_class = UnitCreateUpdateSerializer