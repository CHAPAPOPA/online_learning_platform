from rest_framework.routers import SimpleRouter

from .apps import CourseConfig
from .views import CourseViewSet

app_name = CourseConfig.name

router = SimpleRouter()
router.register("", CourseViewSet, basename="course")

urlpatterns = []

urlpatterns += router.urls
