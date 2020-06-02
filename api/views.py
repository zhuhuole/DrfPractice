from rest_framework.views import APIView
from utils.response import APIResponse
from . import models, serializers
from rest_framework import response


# Create your views here.


class BookAPIView(APIView):

    def get(self, request, *args, **kwargs):

        book_obj = models.Book.objects.all()
        print('book_obj', book_obj)
        book_ser = serializers.BookModelSerializer(book_obj, many=True)
        print('book_ser', book_ser)
        print('book_ser.data', book_ser.data)
        return APIResponse(0, 'ok', results=book_ser.data)
