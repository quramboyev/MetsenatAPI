from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from students.views import StudentViewSet
from sponsors.views import SponsorViewSet, SponsorToStudentViewSet


router = DefaultRouter()
router.register(r'sponsors', SponsorViewSet)
router.register(r'sponsor-to-student', SponsorToStudentViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]