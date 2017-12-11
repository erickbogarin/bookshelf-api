from django.conf.urls import include, url
from rest_framework import routers
from apps.profiles import views

router = routers.DefaultRouter()
router.register(r'authors', views.AuthorSerializer)

urlpatterns = [
    url(r'^', include(router.urls)),
]