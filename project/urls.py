from django.urls import path, include
from .views import BlogViewSet
from rest_framework.routers import DefaultRouter
from rest_framework import urls

router = DefaultRouter()
# 첫 번째 인자는 url의 prefix
# 두 번째 인자는 ViewSet
router.register('blog', BlogViewSet)

urlpatterns =[
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]