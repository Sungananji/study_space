from django.db import models
from django.contrib.auth.models import User
import os

from ckeditor.fields import RichTextField

# Create your models here.
def user_directory_path(instance, filename):
	#THis file will be uploaded to MEDIA_ROOT /the user_(id)/the file
	return 'user_{0}/{1}'.format(instance.user.id, filename)

# Create your models here.
class AssignmentFileContent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory_path)
    posted = models.DateTimeField(auto_now_add=True)
    
    def get_file_name(self):
        return os.path.basename(self.file.name)
    
class Assignment(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title', null=True)
    content = RichTextField()
    files = models.ManyToManyField(AssignmentFileContent)
    points = models.PositiveIntegerField()
    due = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Submission(models.Model):
    file = models.FileField(upload_to=user_directory_path)
    comment = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def get_file_name(self):
        return os.path.basename(self.file.name)