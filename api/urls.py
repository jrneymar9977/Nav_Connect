from django.urls import path
from . import views

urlpatterns = [
    path('driver-detail/<str:pk>',views.driverdetail,name='driver-detail'),
    path('create-driver/',views.createdriver,name='createdriver'),
    path('update-driver/<str:pk>',views.updatedriver,name='updatedriver'),
    path('delete-driver/<str:pk>',views.deletedriver,name='deletedriver'),
]