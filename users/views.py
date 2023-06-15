from rest_framework.views import APIView, Request, Response, status

from .models import User
from .serializers import UserSerializer


class UserView(APIView):
    # authentication_classes = []
    # permission_classes = []

    def post(self, request: Request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request: Request):
        user = User.objects.all()
        serializer = UserSerializer(instance=user, many=True)

        return Response(data=serializer.data)
