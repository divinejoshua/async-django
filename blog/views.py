from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import time
from asgiref.sync import sync_to_async
# Create your views here.



#Synchronous View
class BlogView(APIView):

    # Async function
    def get(self, request, format=None):
        data = {}
        start_time = time.time()
        total_time = (time.time() - start_time)
        data['name'] = "Divine"
        data['type'] = "Sync"
        data['total_time'] = total_time
        return Response(data,  status=status.HTTP_200_OK)



# View heavy task
class BlogAsyncView(APIView):

    # Async function
    def get(self, request, format=None):
        data = {}
        start_time = time.time()

        # Heavy funtion
        mock_heavy_function(10)
        total_time = (time.time() - start_time)

        data['name'] = "Divine"
        data['type'] = "Async"
        data['total_time'] = total_time
        return Response(data,  status=status.HTTP_200_OK)


# # View heavy task (Param)
class BlogAsyncParamView(APIView):

    # Async function
    def get(self, request, request_time: int, format=None):
        data = {}

        start_time = time.time()

        # Heavy funtion
        mock_heavy_function(request_time)
        total_time = (time.time() - start_time)

        data['name'] = "Divine"
        data['type'] = "Async"
        data['request_time'] = request_time
        data['total_time'] = total_time
        return Response(data,  status=status.HTTP_200_OK)




# Heavy Function representation
def mock_heavy_function(operation_time):
    time.sleep(operation_time)
    return True