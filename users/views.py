from utils.genericAPIView import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .permissions import IsAccountOwner


class UserView(CreateAPIView):
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = UserSerializer
    queryset = User.objects.all()
