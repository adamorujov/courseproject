from rest_framework.views import APIView
from rest_framework.generics import (ListAPIView, 
CreateAPIView, 
RetrieveAPIView,
UpdateAPIView,
RetrieveUpdateAPIView,
DestroyAPIView,
get_object_or_404
)

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from account.api.serializers import (AccountSerializer, 
RegisterSerializer, 
CourseListSerializer, 
CourseCreateUpdateDestroySerializer,
UnitDestroySerializer,
UnitCreateUpdateSerializer,
HomeWorkSerializer, 
ListeningSerializer,
ListeningResultSerializer,
ReadingResultSerializer,
)

from rest_framework.response import Response

from account.api.permissions import IsOwner, IsTeacher
from account.models import (
    Account, Course, Unit,
    HomeWork, Listening, ListeningResult, ReadingResult,
    )

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
    serializer_class = CourseCreateUpdateDestroySerializer
    permission_classes = (IsAdminUser,)

class CourseUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = "pk"
    queryset = Course.objects.all()
    serializer_class = CourseCreateUpdateDestroySerializer
    permission_classes = (IsAdminUser,)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class CourseDestroyAPIView(DestroyAPIView):
    lookup_field = "pk"
    queryset = Course.objects.all()
    serializer_class = CourseCreateUpdateDestroySerializer
    permission_classes = (IsAdminUser,)


class UnitCreateAPIView(CreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitCreateUpdateSerializer

class UnitUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = "pk"
    queryset = Unit.objects.all()
    serializer_class = UnitCreateUpdateSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class UnitDestroyAPIView(DestroyAPIView):
    lookup_field = "pk"
    queryset = Unit.objects.all()
    serializer_class = UnitDestroySerializer
    permission_classes = (IsTeacher, )


class HomeWorkListAPIView(ListAPIView):
    queryset = HomeWork.objects.all()
    serializer_class = HomeWorkSerializer

class AccountHomeWorkListAPIView(ListAPIView):
    def get_queryset(self):
        return HomeWork.objects.filter(course__accounts=self.request.user)
    serializer_class = HomeWorkSerializer
    permission_classes = (IsAuthenticated,)

class ListeningListAPIView(ListAPIView):
    queryset = Listening.objects.all()
    serializer_class = ListeningSerializer

class ListeningResultsListAPIView(ListAPIView):
    queryset = ListeningResult.objects.all()
    serializer_class = ListeningResultSerializer
    permission_classes = (IsAdminUser,)

class AccountListeningResultsListAPIView(ListAPIView):
    def get_queryset(self):
        return ListeningResult.objects.filter(account=self.request.user)

    serializer_class = ListeningResultSerializer
    permission_classes = (IsAuthenticated,)


class ReadingResultsListAPIView(ListAPIView):
    queryset = ReadingResult.objects.all()
    serializer_class = ReadingResultSerializer
    permission_classes = (IsAdminUser,)

class AccountReadingResultsListAPIView(ListAPIView):
    def get_queryset(self):
        return ReadingResult.objects.filter(account=self.request.user)

    serializer_class = ReadingResultSerializer
    permission_classes = (IsAuthenticated,)

# class AccountHomeWorkResultsListAPIView(ListAPIView):
#     def get_queryset(self):
#         return HomeWorkResult.objects.filter(account=self.request.user)

#     serializer_class = HomeWorkResultSerializer
#     permission_classes = (IsAuthenticated,)

#     """ text HTML hypertext language has"""