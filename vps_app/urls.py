from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VPSListView, VPSCreateView, VPSUpdateView, VPSDeleteView, VPSViewSet

router = DefaultRouter()
router.register(r'vps', VPSViewSet)


urlpatterns = [
    path('', VPSListView.as_view(), name='vps_list'),
    path('create/', VPSCreateView.as_view(), name='vps_create'),
    path('<int:pk>/update/', VPSUpdateView.as_view(), name='vps_update'),
    path('<int:pk>/delete/', VPSDeleteView.as_view(), name='vps_delete'),
    path('api/', include(router.urls)),
]
