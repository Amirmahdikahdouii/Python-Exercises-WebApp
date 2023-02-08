from django.contrib.auth.models import User
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer


class UserRegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        if password1 == password2 and not User.objects.filter(username=username).exists():
            User.objects.create_user(username, password=password1, )
            return Response(status=201)
        # {"username": "ali", "password1": "ali", "password2": "ali"}
        return Response(status=403)


class CheckUsernameView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        status = User.objects.filter(username=request.data.get("username")).exists()
        return Response({"status": status})


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
