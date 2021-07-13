from rest_framework.routers import DefaultRouter
from . import viewsets

router = DefaultRouter()
router.register(r'clients', viewsets.ClientViewSet, basename='clients')
router.register(r'credit_requests', viewsets.CreditRequestViewset, basename='credit_requests')

urlpatterns = router.urls