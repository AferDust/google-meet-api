from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class TestAPIView(APIView):

    def get(self, request):
        return Response(data="Hello i passed test", status=status.HTTP_200_OK)


