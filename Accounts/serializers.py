from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["userData"] = {
            "id": self.user.id,
            "username": self.user.username,
            "email": self.user.email,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
        }
        return data
