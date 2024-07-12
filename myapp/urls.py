# Manually created.....

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, add_user, update_user, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_user, name='add_user'),
    path('update/<int:id>/', update_user, name='update_user'),
    path('api/', include(router.urls)),
]
