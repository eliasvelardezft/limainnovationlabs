from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token

from .models import Client, CreditRequest
from .serializers import ClientSerializer, CreditRequestSerializer

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

class CreditRequestViewset(viewsets.ModelViewSet):
    serializer_class = CreditRequestSerializer
    queryset = CreditRequest.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    # @action(methods=['PATCH'], detail=True)
    # def change_request_status(self, request, pk=None):
    #     serializer = self.get_serializer(data=request.data)
    #     print(request.data)
    #     serializer.is_valid(raise_exception=True)
    #     credit_request = self.get_object()
    #     new_state = serializer.validated_data['new_state']
    #     CreditRequest.objects.change_request_status(credit_request.pk, new_state)
    #     return Response(serializer.data)