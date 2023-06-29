from django.contrib import admin
from .models import Votes, Answer, Question

# Register your models here.
admin.site.register(Votes)
admin.site.register(Answer)
admin.site.register(Question)