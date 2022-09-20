from django.contrib import admin
from .models import User, Quiz, Question, Option, Score

# Register your models here.

admin.site.register(User)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Score)