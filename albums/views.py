from rest_framework.generics import ListAPIView,  CreateAPIView
from .models import Album
from .serializers import AlbumSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class AlbumView(ListAPIView,  CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
