from django.urls import path
<<<<<<< HEAD
from .views import CreateBus, BusDetails, CreateRoute, DriverView, TestEsp32
=======
from .views import CreateBus, BusDetails, CreateRoute, DriverView, SearchRoute
>>>>>>> 7f5b00cfeae818b2e0e3748f73fddc93de3f3f3c

urlpatterns = [
    path('drivers/', DriverView.as_view(), name='driver-detail'),
    # path('drivers/create/', CreateDriver.as_view(), name='create-driver'),
    # path('drivers/update/<int:pk>/', UpdateDriver.as_view(), name='update-driver'),
    # path('drivers/delete/<int:pk>/', DeleteDriver.as_view(), name='delete-driver'),
    path('createbus/', CreateBus.as_view(), name='create_bus_api'),
    path('createroute/', CreateRoute.as_view(), name='create_route_api'),
    path('busdetails/', BusDetails.as_view(), name='bus_create_api'),
<<<<<<< HEAD
    path("esp32/", TestEsp32.as_view(), name="test esp32")
=======
    path('searchroute/', SearchRoute.as_view(), name='search_route_api'),
>>>>>>> 7f5b00cfeae818b2e0e3748f73fddc93de3f3f3c
]
