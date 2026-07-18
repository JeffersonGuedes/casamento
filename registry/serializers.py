from rest_framework import serializers
from .models import Gift

class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = [
            'id', 
            'name', 
            'description', 
            'category', 
            'price', 
            'image_base64', 
            'status', 
            'buyer_name',
            'updated_at'
        ]
        read_only_fields = ['id', 'status', 'buyer_name', 'updated_at']