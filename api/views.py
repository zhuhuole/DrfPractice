from django.shortcuts import render
from rest_framework.views import APIView
from utils.response import APIResponse

# Create your views here.


class TestAPIView(APIView):
    def get(self, request, *args, **kwargs):

        return APIResponse(0, 'get ok')