from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet,  CategoryViewSet, ProductViewSet, CustomAuthToken

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('login/', CustomAuthToken.as_view(), name='api_login'),
]
