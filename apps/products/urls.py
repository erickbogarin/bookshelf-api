from django.conf.urls import url, include
from rest_framework import routers

from apps.products import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]