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
]
