from rest_framework import routers
from django.conf.urls import url, include

from risk_management.risk_type.views import RiskTypeViewSet

router = routers.SimpleRouter()
router.register(r'risks', RiskTypeViewSet)


urlpatterns = [
    url(r'^', include(router.urls))
]