from rest_framework import serializers
from .models import Garment

class GarmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Garment
        #fields = '__all__'
        fields = ['_id','product_id', 'gender', 'product_title','product_description', 'price', 'stock']

