from rest_framework import serializers
from movies.models.customer_model import CustomerModel


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerModel
        fields = ['id', 'first_name', 'last_name', 'email']
        read_only_fields = ['id']
