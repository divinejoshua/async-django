from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import time
# Create your views here.


class BlogView(APIView):

    # Async function
    def get(self, request, format=None):
        data = {}
        time.sleep(5)
        data['name'] = "Divine"
        return Response(data,  status=status.HTTP_200_OK)