from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order, OrderItem
from .serializers import OrderSerializer, MyOrderSerializer


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serialzer = OrderSerializer(data=request.data)

    if serialzer.is_valid():
        # stripe key fetch from settings
        paid_amount = sum(item.get(
            'quantity')*item.get('product').price for item in serialzer.validated_data['items'])

        try:
            # charge using stripe
            serialzer.save(user=request.user, paid_amount=paid_amount)
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        order = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(order, many=True)
        return Response(serializer.data)
