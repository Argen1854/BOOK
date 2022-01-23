from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.BookList)
admin.site.register(models.BookComment)
admin.site.register(models.Expert)
admin.site.register(models.ExpertRecomendation)