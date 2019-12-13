from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.conf import settings

class CustomPagination(PageNumberPagination):
    page_size = settings.REST_FRAMEWORK.get('PAGE_SIZE')
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            # 'page_size': self.page_size,
            
            'results': data
        })

# Generate random string
import binascii
import os
def generate_key():		
    return binascii.hexlify(os.urandom(20)).decode()

