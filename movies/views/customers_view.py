from rest_framework.viewsets import ModelViewSet

from movies.models.customer_model import CustomerModel
from movies.serializers.customer_serializer import CustomerSerializer


class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = CustomerModel.objects.all()

    def get_queryset(self):
        return self.queryset.filter(store_id=self.kwargs.get('store_id'))