from rest_framework.views import Request, Response, status


class CreateModelMixin:

    def create(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


# class ReadModelMixin:
#     def read(self, request: Request) -> Response:
#         queryset = self.queryset.all()
#         serializer = self.serializer_class(queryset, many=True)
#         return Response(serializer.data)