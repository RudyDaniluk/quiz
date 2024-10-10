from django.contrib import admin
from .models import Course, Test, Question, Answer, Result

admin.site.register(Course)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Result)
