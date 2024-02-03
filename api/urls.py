from django.urls import path
from .views import DriverDetail, CreateDriver, UpdateDriver, DeleteDriver, BusCreation, BusDetails

urlpatterns = [
    path('drivers/<int:pk>/', DriverDetail.as_view(), name='driver-detail'),
    path('drivers/create/', CreateDriver.as_view(), name='create-driver'),
    path('drivers/update/<int:pk>/', UpdateDriver.as_view(), name='update-driver'),
    path('drivers/delete/<int:pk>/', DeleteDriver.as_view(), name='delete-driver'),
    path('createbus/', BusCreation.as_view(), name='create_bus_api'),
    path('busdetails/', BusDetails.as_view(), name='create_bus_api'),
]
