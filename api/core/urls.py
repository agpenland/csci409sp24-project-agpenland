from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VesselViewSet
from .views import VesselScheduleViewSet
from .views import BillOfLadingViewSet
from .views import ContainerViewSet

router = DefaultRouter()
router.register(r'vessels', VesselViewSet, basename = 'vessel')
router.register(r'vessel_schedules', VesselScheduleViewSet, basename = 'vessel_schedule')
router.register(r'bill_of_ladings', BillOfLadingViewSet, basename = 'bill_of_lading')
router.register(r'containers', ContainerViewSet, basename = 'container')

urlpatterns = {
    path('', include(router.urls)),
}
