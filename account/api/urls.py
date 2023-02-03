from django.urls import path
from account.api import views

urlpatterns = [
    path('accounts/', views.AccountListAPIView.as_view(), name="accounts"),
    path('register/', views.RegisterAPIView.as_view(), name="register"),
    path('account/<email>/', views.AccountRetrieveAPIView.as_view(), name="account"),
    path('courses/', views.CourseListAPIView.as_view(), name="courses"),
    path('mycourses/', views.AccountCoursesListAPIView.as_view(), name="mycourses"),
    path('course-create/', views.CourseCreateAPIView.as_view(), name="coursecreate"),
    path('course-update/<int:pk>/', views.CourseUpdateAPIView.as_view(), name="course-update"),
    path('course-delete/<int:pk>/', views.CourseDestroyAPIView.as_view(), name="course-delete"),
    path('unit-create/', views.UnitCreateAPIView.as_view(), name="unit-create"),
    path('unit-update/<int:pk>/', views.UnitUpdateAPIView.as_view(), name="unit-update"),
    path('unit-delete/<int:pk>/', views.UnitDestroyAPIView.as_view(), name="unit-delete"),
    path('homeworks/', views.HomeWorkListAPIView.as_view(), name="homeworks"),
    path('myhomeworks/', views.AccountHomeWorkListAPIView.as_view(), name="myhomeworks"),
    path('listenings/', views.ListeningListAPIView.as_view(), name="listenings"),
    # path('listeningresults/', views.ListeningResultsListAPIView.as_view(), name="listeningresults"),
    # path('readingresults/', views.ReadingResultsListAPIView.as_view(), name="readingresults"),
    # path('mylisteningresults/', views.AccountListeningResultsListAPIView.as_view(), name="mylisteningresults"),
    # path('myreadingresults/', views.AccountReadingResultsListAPIView.as_view(), name="myreadingresults"),
    path('myhomeworkresults/', views.AccountHomeWorkResultsListAPIView.as_view(), name="myhomeworkresults"),
]
