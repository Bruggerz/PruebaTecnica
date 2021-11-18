from rest_framework import fields, serializers
from rest_framework.relations import PrimaryKeyRelatedField
from restaurant.models import Restaurant

class Restaurant(serializers.ModelSerializer):
    class Meta:
        model=Restaurant
        fields="__all__"
