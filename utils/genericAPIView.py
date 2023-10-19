from rest_framework.views import APIView, Request, Response
from .mixins import CreateModelMixin


class GenericAPIView(APIView):
    serializer_class = None
    queryset = None


class CreateAPIView(GenericAPIView, CreateModelMixin):
    def post(self, request: Request) -> Response:
        return super().create(request)


