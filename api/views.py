from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DriverSerializer, BusSerializer, RoutesSerializer, SubRoutesSerializer
from .models import Driver, Bus, Routes, Location, SubRoutes, User
from routestTest import getBusDetails 


class DriverView(APIView):
    def get(self, request):
        drivers = Driver.objects.all()
        serializer_all = DriverSerializer(drivers, many=True)
        pk = request.data.get("pk")
        if pk:
            driver = Driver.objects.get(id=pk)
            serializer_specific = DriverSerializer(driver)
            return Response({
                'all_drivers': serializer_all.data,
                'specific_driver': serializer_specific.data
            })
        else:
            return Response(serializer_all.data)
        
    def post(self, request):
        user = User.objects.create_user(**request.data.get("user"))
        d = dict(request.data)
        d["user"] = user.id
        driverserializer = DriverSerializer(data=d)
        if driverserializer.is_valid():
            driverserializer.save()
            return Response(driverserializer.data, status=status.HTTP_201_CREATED)
        return Response("error", status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        driver = Driver.objects.get(id=pk)
        serializer = DriverSerializer(instance=driver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        driver = Driver.objects.get(id=pk)
        driver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

   

#check if the driver not allocated to any bus


# class BusCreation(APIView):
#     def post(self, request):
#         serializer = BusCreationSerializer(data=request.data)
#         if serializer.is_valid():
#             bus_no = serializer.validated_data['bus_no']
#             driver = Driver.objects.all()[0]
#             bus = Bus.objects.create(busno=bus_no, driver=driver)
            # routes_data = serializer.validated_data['routes']
            # print(Driver.objects.all())
            # location_bus = Location.objects.create(current_latitude=0, current_longitude=0)
            # for route_data in routes_data:
            #     routename = route_data['route_name']
            #     order = route_data['order']
            #     lat = route_data['lat']
            #     lang = route_data['lang']
            #     location = Location.objects.create(current_latitude=lat, current_longitude=lang)
            #     route = SubRoutes.objects.create(route_name=routename, order=order, location=location,bus_id=bus.id)
        #     return Response("Bus and routes created successfully", status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
    

class CreateBus(APIView):
    def post(self, request):
        serializer = BusSerializer(data=request.data)
        
        if serializer.is_valid():
            bus = serializer.save()
            bus.location = Location.objects.create();
            bus.save()
            # Return success response with serialized data of the created bus
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Return error response with serializer errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
        
class BusDetails(APIView):
    def get(self, request):
        buses = Bus.objects.all() #add query that driver and route is not null
        bus_data = []
        for bus in buses:
            driver_name = bus.driver.name
            if(bus.location != None):
                bus_lat = bus.location.current_latitude 
                bus_lang = bus.location.current_longitude 
            else:
                bus_lat = 0.0 
                bus_lang = 0.0

            route_id = bus.route
            route_data = []
            routes = SubRoutes.objects.filter(route=route_id.id)
            print(routes)
            for route in routes:
                route_data.append( {
                    "route_name": route.route_name,
                    "order": route.order,
                    "lat": route.location.current_latitude,
                    "lang": route.location.current_longitude
                })
            
            bus_details = {
                "route_id": route_id.id,
                "bus_id": bus.id,
                "bus_no": bus.busno,
                "driver_id": bus.driver.id,
                "driver_name": driver_name,
                "bus_lat": bus_lat,
                "bus_lang": bus_lang,
                "route_title" : route_id.route_title,
                "routes": route_data
            }
            bus_data.append(bus_details)
        
        return Response(bus_data)

test_route = {
    "route" : "porur",
    "subroutes" : [
        {
            "route_name" : "Velachery",
            "lat" : 23.2,
            "lang" : 21.2
        },
        {
            "route_name" : "Velachery",
            "lat" : 23.2,
            "lang" : 21.2
        },
        {
            "route_name" : "Velachery",
            "lat" : 23.2,
            "lang" : 21.2
        },
    ]
}

class CreateRoute(APIView):
    def post(self, request):
        route_data = request.data.get('route_title', "")
        subroutes_data = request.data.get('subroutes', [])
        print(route_data)
        print(subroutes_data[0])
        # Validate route data
        route_serializer = RoutesSerializer(data=request.data)
        # print("route_serializer : ")
        # print(route_serializer)
        if not route_serializer.is_valid():
            print("route title not created")
            return Response(route_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Save route
        route_instance = route_serializer.save()

        # Validate and save subroutes
        for subroute_data in subroutes_data:
            subroute_data['route'] = route_instance.id  # Associate subroute with the route
            print(subroute_data)
            loc = subroute_data["location"]
            loc_instance = Location.objects.create(current_latitude=loc["lat"], current_longitude=loc["lang"])
            subroute_data["location"] = loc_instance.id
            subroute_serializer = SubRoutesSerializer(data=subroute_data)
            # print(subroute_serializer)
            if subroute_serializer.is_valid():
                subroute_serializer.save()
            else:
                print("sub route not created")
                # Rollback the route creation if subroute creation fails
                route_instance.delete()
                return Response(subroute_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"response" : "ok" }, status=status.HTTP_201_CREATED)
   
class TestEsp32(APIView):
    def get(self, request):
        print("get method")
        print(request.query_params )
        print(request.data)
        return Response("respone ok", status=status.HTTP_200_OK)
    def post(self, request):
        print("post method")
        print(request.data)
        return Response("respone ok", status=status.HTTP_200_OK)