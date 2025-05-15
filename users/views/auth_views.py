# users/views/auth_views.py
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from users.serializers.auth_serializers import UserRegisterSerializer, UserLoginSerializer

# View لتسجيل المستخدم
class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {'message': 'تم التسجيل بنجاح!'},
            status=status.HTTP_201_CREATED
        )

# View لتسجيل الدخول
class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        # توليد توكن JWT
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response(
            {
                'message': 'تم تسجيل الدخول بنجاح!',
                'access_token': access_token,
                'refresh_token': str(refresh),
            },
            status=status.HTTP_200_OK
        )
