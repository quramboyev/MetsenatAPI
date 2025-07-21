from django.contrib import admin
from .models import SponsorModel, SponsorToStudentModel

admin.site.register(SponsorModel)
admin.site.register(SponsorToStudentModel)
