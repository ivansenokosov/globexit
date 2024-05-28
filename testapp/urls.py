app_name = 'testapp'

from testapp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('globexit', views.GlobexUsersViewset, 'globexit')

urlpatterns = router.urls
