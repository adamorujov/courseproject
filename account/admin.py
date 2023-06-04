from django.contrib import admin
from account.models import (
    Account, Course, Unit,
    HomeWork, Listening, ListeningQuestion, ListeningQuestionAnswer, ListeningResult,
    Reading, ReadingAnswer, ReadingResult, Certificate, Resource,
    CourseGroup, GroupLesson, CheckIn
)

admin.site.register(Account)
admin.site.register(Course)
admin.site.register(Unit)
admin.site.register(HomeWork)
admin.site.register(Listening)
admin.site.register(ListeningQuestion)
admin.site.register(ListeningQuestionAnswer)
admin.site.register(ListeningResult)
admin.site.register(Reading)
admin.site.register(ReadingAnswer)
admin.site.register(ReadingResult)
admin.site.register(Certificate)
admin.site.register(Resource)

admin.site.register(CourseGroup)
admin.site.register(GroupLesson)
admin.site.register(CheckIn)