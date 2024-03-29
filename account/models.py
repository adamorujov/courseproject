from django.db import models
from django.contrib import auth
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

ACCOUNT_CHOICES = [
    ('T', 'teacher'),
    ('S', 'student'),
]

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

    def with_perm(self, perm, is_active=True, include_superusers=True, backend=None, obj=None):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    'You have multiple authentication backends configured and '
                    'therefore must provide the `backend` argument.'
                )
        elif not isinstance(backend, str):
            raise TypeError(
                'backend must be a dotted import path string (got %r).'
                % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, 'with_perm'):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()

class Account(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    category = models.CharField(max_length=7, choices=ACCOUNT_CHOICES, default="T")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        ordering = ["-id"]
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    objects = UserManager()

    def __str__(self):
        return self.email

class Course(models.Model):
    accounts = models.ManyToManyField(Account, related_name="courses")
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Unit(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="units")
    name = models.CharField(max_length=256)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class CourseGroup(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_groups")
    accounts = models.ManyToManyField(Account, related_name="group_accounts")
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Group"
    
    def __str__(self):
        return self.name


class HomeWork(models.Model):
    # course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="homeworks") homework
    group = models.ForeignKey(CourseGroup, on_delete=models.CASCADE, related_name="homeworks")
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    
# class HomeWorkResult(models.Model):
#     account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="accounthomeworkresults")
#     def __str__(self):
#         return self.account.email

class Listening(models.Model):
    homework = models.ForeignKey(HomeWork, on_delete=models.CASCADE, related_name="listenings")
    name = models.CharField(max_length=256)
    audio = models.FileField(upload_to="audio/")
    max_result = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class ListeningQuestion(models.Model):
    listening = models.ForeignKey(Listening, on_delete=models.CASCADE, related_name="listeningquestions")
    question = models.TextField()
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.question

class ListeningQuestionAnswer(models.Model):
    question = models.ForeignKey(ListeningQuestion, on_delete=models.CASCADE, related_name="listeningquestionanswers")
    answer = models.CharField(max_length=528)
    is_true = models.BooleanField(default=False)

    def __str__(self):
        return self.answer

class ListeningResult(models.Model):
    # homeworkresult = models.ForeignKey(HomeWorkResult, on_delete=models.CASCADE, related_name="homeworklisteningresults")
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="accountlisteningresults")
    listening = models.ForeignKey(Listening, on_delete=models.CASCADE, related_name="listeningresults")
    result = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.account.email


# class ListeningQuestionAccountAnswer(models.Model):
#     account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="accountlisteningquestionanswer")
#     answer = models.ForeignKey(ListeningQuestionAnswer, on_delete=models.CASCADE, related_name="versions")
#     version = models.CharField(max_length=528)

#     def __str__(self):
#         return self.version


class Reading(models.Model):
    homework = models.ForeignKey(HomeWork, on_delete=models.CASCADE, related_name="readings")
    name = models.CharField(max_length=256)
    text = models.TextField()
    max_result= models.IntegerField(default=0)

    def __str__(self):
        return self.name

class ReadingAnswer(models.Model):
    reading = models.ForeignKey(Reading, on_delete=models.CASCADE, related_name="readinganswers")
    answer = models.CharField(max_length=256)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.answer


class ReadingResult(models.Model):
    # homeworkresult = models.ForeignKey(HomeWorkResult, on_delete=models.CASCADE, related_name="homeworkreadingresults")
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="accountreadingresults")
    reading = models.ForeignKey(Reading, on_delete=models.CASCADE, related_name="readingresults")
    result = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.account.email

class Certificate(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="account_certificates")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_certificates")
    certificate = models.FileField(upload_to="certificates/")
    score = models.FloatField(default=0)

    def __str__(self):
        return self.account.username + "|" + self.course.name

class Resource(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="resources")
    name = models.CharField(max_length=528)
    resource = models.FileField(upload_to="resources/")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name 

class GroupLesson(models.Model):
    group = models.ForeignKey(CourseGroup, on_delete=models.CASCADE, related_name="group_lessons")
    name = models.CharField(max_length=256)
    date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Group Lesson"
        verbose_name_plural = "Group Lessons"

    def __str__(self):
        return self.name

class CheckIn(models.Model):
    grouplesson = models.ForeignKey(GroupLesson, on_delete=models.CASCADE, related_name="grouplesson_checkins")
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="account_checkins")

    class Meta:
        verbose_name = "Check-In"
        verbose_name_plural = "Check-In"

    def __str__(self):
        return self.grouplesson.name + " - " + self.account.first_name + " " + self.account.last_name




