from rest_framework import serializers
from ScrapApp.models import BrowseItems


# class cartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = cart
#         fields=['cart_item_name','cart_item_count']

class BrowseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=BrowseItems
        fields=['name','price','description','image_link']