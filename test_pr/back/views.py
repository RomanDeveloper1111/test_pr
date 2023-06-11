from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from back.models import CreditOrder


class ViewUniqueProducer(GenericViewSet):

    @action(methods=["GET", ], detail=True)
    def unique_producers(self, request, pk=None):
        instances = get_object_or_404(CreditOrder, contract__pk=pk).credit_products.\
            distinct('producer').only('producer')
        return Response({'name': [el.producer.name for el in instances]}, status=status.HTTP_200_OK)
