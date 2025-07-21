from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from students.views import StudentViewSet, UniversityViewSet
from sponsors.views import SponsorViewSet, SponsorToStudentViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


router = DefaultRouter()
router.register(r'sponsors', SponsorViewSet)
router.register(r'sponsor-to-student', SponsorToStudentViewSet)
router.register(r'students', StudentViewSet)
router.register(r'universities', UniversityViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]