from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("courses/", include("course.urls", namespace="courses")),
    path("lessons/", include("lesson.urls", namespace="lessons")),
    path('users/', include('users.urls', namespace='payments')),
]
