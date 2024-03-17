from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DriverSerializer, BusCreationSerializer
from .models import Driver, Bus, Location, Routes, User
from routestTest import getBusDetails 


class DriverDetail(APIView):
    def get(self, request, pk):
        driver = Driver.objects.get(id=pk)
        serializer = DriverSerializer(driver)
        return Response(serializer.data)

class CreateDriver(APIView):
    def post(self, request):
        user = User.objects.create_user(**request.data.get("user"))
        d = dict(request.data)
        d["user"] = user.id
        driverserializer = DriverSerializer(data=d)
        if driverserializer.is_valid():
            driverserializer.save()
            return Response(driverserializer.data, status=status.HTTP_201_CREATED)
        return Response("error", status=status.HTTP_400_BAD_REQUEST)

class UpdateDriver(APIView):
    def post(self, request, pk):
        driver = Driver.objects.get(id=pk)
        serializer = DriverSerializer(instance=driver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteDriver(APIView):
    def delete(self, request, pk):
        driver = Driver.objects.get(id=pk)
        driver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BusCreation(APIView):
    def post(self, request):
        serializer = BusCreationSerializer(data=request.data)
        if serializer.is_valid():
            bus_no = serializer.validated_data['bus_no']
            driver_id = serializer.validated_data['driver_id']
            routes_data = serializer.validated_data['routes']
            
            # print(Driver.objects.all())
            driver = Driver.objects.all()[0]
            
            location_bus = Location.objects.create(current_latitude=0, current_longitude=0)
            bus = Bus.objects.create(busno=bus_no, driver=driver,location=location_bus)
            
            for route_data in routes_data:
                routename = route_data['route_name']
                order = route_data['order']
                lat = route_data['lat']
                lang = route_data['lang']

                location = Location.objects.create(current_latitude=lat, current_longitude=lang)
                route = Routes.objects.create(route_name=routename, order=order, location=location,bus_id=bus.id)
                

            return Response("Bus and routes created successfully", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class BusDetails(APIView):
#     def get(self, request):
#         buses = Bus.objects.all()
#         bus_data = []
#         for bus in buses:
#             driver_name = bus.driver.name 
#             bus_lat = bus.location.current_latitude 
#             bus_lang = bus.location.current_longitude 
            
#             routes_data = []
#             routes = Routes.objects.filter(bus_id=bus.id)
#             for route in routes:
#                 route_data = {
#                     "route_name": route.route_name,
#                     "order": route.order,
#                     "lat": route.location.current_latitude,
#                     "lang": route.location.current_longitude
#                 }
#                 routes_data.append(route_data)
            
#             bus_details = {
#                 "bus_id": bus.id,
#                 "bus_no": bus.busno,
#                 "driver_id": bus.driver.id,
#                 "driver_name": driver_name,
#                 "bus_lat": bus_lat,
#                 "bus_lang": bus_lang,
#                 "routes": routes_data
#             }
#             bus_data.append(bus_details)
#         newBuses = getBusDetails()
#         print("newBuses")
#         bus_data += newBuses
#         print(bus_data)
#         return Response(bus_data)
    
class BusDetails(APIView):
    def get(self, request):
        buses = Bus.objects.all()
        bus_data = []
        for bus in buses:
            driver_name = bus.driver.name 
            bus_lat = bus.location.current_latitude 
            bus_lang = bus.location.current_longitude 
            
            route_data = []
            routes = Routes.objects.filter(bus_id=bus.id)
            for route in routes:
                route = {
                    "route_name": route.route_name,
                    "order": route.order,
                    "lat": route.location.current_latitude,
                    "lang": route.location.current_longitude
                }
                route_data.append(route)
            
            bus_details = {
                "bus_id": bus.id,
                "bus_no": bus.busno,
                "driver_id": bus.driver.id,
                "driver_name": driver_name,
                "bus_lat": bus_lat,
                "bus_lang": bus_lang,
                "routes": route_data
            }
            bus_data.append(bus_details)
        
        return Response(bus_data)

