from django.shortcuts import render
from  rest_framework.views import APIView
from  rest_framework.response import Response
from rest_framework import status
from .models import User ,Property ,PropertyUser
import secrets
# Create your views here.


# class UserLoginDetails(APIView):

#     def post(self, request):
#         username = request.data.get('username')
#         phone = request.data.get('phone')

#         if not username or not phone:
#             return Response(
#                 {"error": "Username and phone are required"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         try:
#             user = User.objects.get(username=username, phone=phone)

#             return Response(
#                 {
#                     "message": "Login successful",
#                     "user_id": user.id,
#                     "username": user.username,
#                     "phone": user.phone,
#                 },
#                 status=status.HTTP_200_OK
#             )

#         except User.DoesNotExist:
#             return Response(
#                 {"error": "Invalid credentials"},
#                 status=status.HTTP_401_UNAUTHORIZED
#             )



class PropertyFilter(APIView):

    def get(self, request):
        """
        GET /api/properties/ 
        Optional query params: bhk, locations, price_min, price_max
        """
        bhk = request.query_params.get('bhk')
        locations = request.query_params.getlist("locations")  # support multiple locations
        price_min = request.query_params.get('price_min')
        price_max = request.query_params.get('price_max')

        

        query = Property.objects.all()

        if bhk:
            bhk = bhk + "BHK"

            query = query.filter(bhk=bhk)


        if locations:
            query = query.filter(location__in=locations or property)

        if price_min is not None:
            query = query.filter(price__gte=price_min)

        if price_max is not None:
            query = query.filter(price__lte=price_max)

        properties_list = list(
            query.values(
                "id",
                "property_name",
                "description",
                "price",
                "property_type",
                "brochure",
                "pincode",
                "address",
                "location",
                "country",
                "status",
                "created_at",
                "updated_at",
                "bhk"
            )
        )

        return Response(properties_list, status=status.HTTP_200_OK)

    def post(self, request):
        """
        POST /api/properties/filter/
        Body: { bhk, locations, price_min, price_max }
        """
        data = request.data
        bhk = data.get('bhk')
        locations = data.get("locations")  
        price_min = data.get("price_min")
        price_max = data.get("price_max")

        query = Property.objects.all()

        if bhk:
            bhk = bhk + "BHK"
            print(bhk,"ddddd")
            query = query.filter(bhk=bhk)

        if locations:
            if isinstance(locations, list):
                query = query.filter(location__in=locations)
            else:
                query = query.filter(location__icontains=locations)

        if price_min is not None:
            query = query.filter(price__gte=price_min)
        if price_max is not None:
            query = query.filter(price__lte=price_max)

        properties_list = list(
            query.values(
                "id",
                "property_name",
                "description",
                "price",
                "property_type",
                "brochure",
                "pincode",
                "address",
                "location",
                "country",
                "status",
                "created_at",
                "updated_at",
                "bhk"
            )
        )

        return Response(properties_list, status=status.HTTP_200_OK)





class UserRegistrationsView(APIView):

    def post(self, request):
        data = request.data 
        username = data.get("username")
        email = data.get('email')
        phone  = data.get('phone')
        if not [username , email , phone]:
            return Response({
                'message' : "Some field is missing" ,
                'status' :  400
            })
        obje  = User.objects.create(
            username =username,
            email = email,
            phone = phone
        )
        
        session_id = secrets.token_hex(32)

        return Response({
            'message' : "Thank for Registrations " ,
            'status' : 200 ,
            'session_id' :session_id ,
            "username" : username ,
            "email" : email  ,
            "phone" : phone
        })







class UserClickSearchProperty(APIView):


    def post(self,request):


        try:

            data = request.data
            username = data.get("username")
            email = data.get('email')
            phone  = data.get('phone')
            user_property_location = data.get('user_property_location')
            user_click_location = data.get('user_click_location')
            is_search = data.get('is_search')
            is_click = data.get('is_click')


            if is_search and user_property_location:
                print("data is coming here")
                PropertyUser(
                    username = username or "",
                    email = email ,
                    phone = phone ,
                    user_click_location = "",
                    is_search = True ,
                    user_property_location = user_property_location

                ).save()


                return Response({
                    "status" :200 ,
                    "ping" : True
                })


            PropertyUser(
                username = username  or '',
                email = email ,
                phone= phone ,
                is_click = is_click,
                user_property_location = "" , 
                user_click_location = user_click_location

            ).save()
            return Response({
                    "status" :200 ,
                    "ping" : True
                })
        except Exception as e :

            return Response({
                "message" : str(e)
            })








