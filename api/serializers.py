from rest_framework import serializers
from . import models


class BookModelSerializer(serializers.Serializer):

    # name = serializers.CharField()
    # price = serializers.DecimalField(max_digits=5, decimal_places=2)
    class Meta:
        model = models.Book
        fields = ('name', 'price')
