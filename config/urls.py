from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("courses/", include("course.urls", namespace="courses")),
    path("lessons/", include("lesson.urls", namespace="lessons")),
    path("users/", include("users.urls", namespace="users")),
    path('subscriptions/', include('subscription.urls', namespace='subscriptions'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
