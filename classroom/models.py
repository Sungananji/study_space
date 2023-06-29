from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


from module.models import Module
from question.models import Question
from assignment.models import Submission
import uuid
# Create your models here.
from ckeditor.fields import RichTextField



STATUS_CHOICES = (
	('pending', 'Pending'),
	('graded', 'Graded'),
)
def user_directory_path(instance, filename):
 # this file will be uploaded to to media_root/ the user(id) file
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Category(models.Model):
	title = models.CharField(max_length=100, verbose_name='Title', null=True)
	icon = models.CharField(max_length=100, verbose_name='Icon', default='article')
	slug = models.SlugField(unique=True)

	def get_absolute_url(self):
		return reverse('categories', arg=[self.slug])

	def __str__(self):
		return self.title


class Course(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	picture = models.ImageField(upload_to=user_directory_path, null=True)
	title = models.CharField(max_length=200, null=True)
	description = models.CharField(max_length=300, null=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
	syllabus = RichTextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_owner')
	enrolled = models.ManyToManyField(User)
	modules = models.ManyToManyField(Module)
	questions = models.ManyToManyField(Question)
    


	def __str__(self):
		return self.title

class Grade(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
	points = models.PositiveIntegerField(default=0)
	graded_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	status = models.CharField(choices=STATUS_CHOICES, default='pending', max_length=10, verbose_name='Status')