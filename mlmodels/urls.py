from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from mlmodels.views import MLAlgorithmViewSet
from mlmodels.views import MLAlgorithmStatusViewSet
from mlmodels.views import MLRequestViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

urlpatterns = [
    url(r"^", include(router.urls)),
]