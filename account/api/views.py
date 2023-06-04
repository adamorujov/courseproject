from rest_framework.views import APIView
from rest_framework.generics import (ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView,
RetrieveUpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView,
get_object_or_404
)

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from account.api.serializers import (AccountSerializer, RegisterSerializer,
CourseListSerializer, CourseCreateUpdateDestroySerializer,
UnitDestroySerializer, UnitCreateUpdateSerializer,
HomeWorkSerializer, ListeningSerializer, ListeningResultSerializer, ReadingResultSerializer,
HomeWorkCreateSerializer, ListeningCreateSerializer, ListeningQuestionCreateSerializer,
ListeningQuestionAnswerCreateSerializer, ReadingCreateSerializer, ReadingAnswerCreateSerializer,
ListeningResultCreateSerializer, ReadingResultCreateSerializer, HomeWorkUpdateDestroySerializer,
ListeningUpdateDestroySerializer, ListeningQuestionUpdateDestroySerializer, ListeningQuestionAnswerUpdateDestroySerializer,
ReadingUpdateDestroySerializer, ReadingAnswerUpdateDestroySerializer,
CertificateListSerializer, ResourceListSerializer,
CourseGroupListSerializer, CourseGroupUpdateDestroySerializer
)

from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from account.api.permissions import IsOwner, IsTeacher, IsTeacherUser, IsStudentUser
from account.models import (
    Account, Course, Unit,
    HomeWork, Listening, ListeningResult, ListeningQuestion, ListeningQuestionAnswer,
    Reading, ReadingAnswer, ReadingResult, Certificate, Resource,
    CourseGroup, GroupLesson, CheckIn
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

class HomeWorkCreateAPIView(CreateAPIView):
    queryset = HomeWork.objects.all()
    serializer_class = HomeWorkCreateSerializer
    permission_classes = (IsTeacherUser,)

class ListeningCreateAPIView(CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = Listening.objects.all()
    serializer_class = ListeningCreateSerializer
    permission_classes = (IsTeacherUser,)

class ListeningQuestionCreateAPIView(CreateAPIView):
    queryset = ListeningQuestion.objects.all()
    serializer_class = ListeningQuestionCreateSerializer
    permission_classes = (IsTeacherUser,)

class ListeningQuestionAnswerCreateAPIView(CreateAPIView):
    queryset = ListeningQuestionAnswer.objects.all()
    serializer_class = ListeningQuestionAnswerCreateSerializer
    permission_classes = (IsTeacherUser,)

class ReadingCreateAPIView(CreateAPIView):
    queryset = Reading.objects.all()
    serializer_class = ReadingCreateSerializer
    permission_classes = (IsTeacherUser,)

class ReadingAnswerCreateAPIView(CreateAPIView):
    queryset = ReadingAnswer.objects.all()
    serializer_class = ReadingAnswerCreateSerializer
    permission_classes = (IsTeacherUser,)

class ListeningResultCreateAPIView(CreateAPIView):
    queryset = ListeningResult.objects.all()
    serializer_class = ListeningResultCreateSerializer
    permission_classes = (IsStudentUser,)

class ReadingResultCreateAPIView(CreateAPIView):
    queryset = ReadingResult.objects.all()
    serializer_class = ReadingResultCreateSerializer
    permission_classes = (IsStudentUser,)

class HomeWorkRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = HomeWork.objects.all()
    lookup_field = "id"
    serializer_class = HomeWorkUpdateDestroySerializer
    permission_classes = (IsTeacher,)

class ListeningRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Listening.objects.all()
    lookup_field = "id"
    serializer_class = ListeningUpdateDestroySerializer
    permission_classes = (IsTeacherUser,)

class ListeningQuestionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ListeningQuestion.objects.all()
    lookup_field = "id"
    serializer_class = ListeningQuestionUpdateDestroySerializer
    permission_classes = (IsTeacherUser,)

class ListeningQuestionAnswerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ListeningQuestionAnswer.objects.all()
    lookup_field = "id"
    serializer_class = ListeningQuestionAnswerUpdateDestroySerializer
    permission_classes = (IsTeacherUser,)

class ReadingRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Reading.objects.all()
    lookup_field = "id"
    serializer_class = ReadingUpdateDestroySerializer
    permission_classes = (IsTeacherUser,)

class ReadingAnswerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ReadingAnswer.objects.all()
    lookup_field = "id"
    serializer_class = ReadingAnswerUpdateDestroySerializer
    permission_classes = (IsTeacherUser,)


class CertificateListAPIView(ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateListSerializer
    permission_classes = (IsAdminUser,)

class ResourceListAPIView(ListAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceListSerializer
    permission_classes = (IsAdminUser,)

class AccountCertificateListAPIView(ListAPIView):
    def get_queryset(self):
        return Certificate.objects.filter(account=self.request.user)

    serializer_class = CertificateListSerializer

class AccountResourceListAPIView(ListAPIView):
    def get_queryset(self):
        return Resource.objects.filter(course__accounts=self.request.user)

    serializer_class = ResourceListSerializer

class CertificateCreateAPIView(CreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateListSerializer
    permission_classes = (IsAdminUser,)

class ResourceCreateAPIView(CreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceListSerializer
    permission_classes = (IsTeacher,)

class CertificateRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateListSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = "id"

class ResourceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceListSerializer
    permission_classes = (IsTeacher,)
    lookup_field = "id"


class CourseGroupListAPIView(ListAPIView):
    queryset = CourseGroup.objects.all()
    serializer_class = CourseGroupListSerializer
    permission_classes = (IsAdminUser,)
    
class AccountCourseGroupListAPIView(ListAPIView):
    def get_queryset(self):
        return CourseGroup.objects.filter(
            accounts = self.request.user
        )
    serializer_class = CourseGroupListSerializer
    permission_classes = (IsAuthenticated,)

class CourseCourseGroupListAPIView(ListAPIView):
    def get_queryset(self, id):
        course = Course.objects.get(id=id)
        return CourseGroup.objects.filter(
            course = course
        )
    serializer_class = CourseGroupListSerializer
    permission_classes = (IsAdminUser,)
    
class CourseGroupCreateAPIView(CreateAPIView):
    queryset = CourseGroup.objects.all()
    serializer_class = CourseGroupUpdateDestroySerializer
    permission_classes = (IsAdminUser,)

class CourseGroupUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_field = "pk"
    queryset = CourseGroup.objects.all()
    serializer_class = CourseGroupUpdateDestroySerializer
    permission_classes = (IsAdminUser,)


