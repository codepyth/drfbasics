from rest_framework import serializers
from .models import *

class WishlistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Whishlist
        fields = ['product_id', 'customer_id']

class ProductSerializer(serializers.ModelSerializer):
    # wishlist = WishlistSerializer(many=True)
    Favourite = serializers.SerializerMethodField(method_name='favourite')
    class Meta:
        model = Product
        fields = ['id', 'name', 'product_code', 'Favourite']
    
    def favourite(self, obj):
        Favourite = Whishlist.objects.filter(product_id__id=obj.id)
        if Favourite:
            return True
        return False