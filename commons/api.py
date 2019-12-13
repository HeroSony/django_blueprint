from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework import status
from subscriber.models import SubscriberAuthToken
from django.shortcuts import get_object_or_404

class APIViewMixin(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field        = 'pk'

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.all()

class RudViewMixin(generics.RetrieveUpdateDestroyAPIView):
    lookup_field        = 'pk'
    
    def get_queryset(self):
        return self.model.objects.all()

def get_subscriber_from_token(request, obj = False):
    auth = request.META.get('HTTP_AUTHORIZATION').split()
    token = auth[1]
    subscriber = get_object_or_404(SubscriberAuthToken, auth_token=token)
    subscriber = subscriber.subscriber

    if obj:
        return subscriber
    
    return subscriber.id


def ResponseSuccess(message = 'Success', data = None):
    return Response({
                'message': message,
                'data': data,
            }, status=status.HTTP_200_OK)

def ResponseError(message = 'Error', data = None):
    return Response({
        'message': message,
        'data': data
    }, status=status.HTTP_400_BAD_REQUEST)
