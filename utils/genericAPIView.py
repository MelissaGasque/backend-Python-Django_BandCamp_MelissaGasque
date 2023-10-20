# Apenas como explicação pelo o que acontece de baixo dos panos!!
from rest_framework.views import APIView, Request, Response
from .mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from .mixins import UpdateModelMixin, DestroyModelMixin


class GenericView(APIView):
    serializer_class = None
    queryset = None


class CreateAPIView(GenericView, CreateModelMixin):
    def post(self, request: Request) -> Response:
        return super().create(request)


class ListAPIView(GenericView, ListModelMixin):
    def get(self, request: Request) -> Response:
        return super().list(request)


class RetrieveAPIView(GenericView, RetrieveModelMixin):
    def get(self, request: Request, pk: int) -> Response:
        return super().retrieve(request, pk)


class UpdateAPIView(GenericView, UpdateModelMixin):
    def patch(self, request: Request, pk: int) -> Response:
        return super().partial_update(request, pk)


class DestroyAPIView(GenericView, DestroyModelMixin):
    def delete(self, request: Request, pk: int) -> Response:
        return super().destroy(request, pk)
