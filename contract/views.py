

# Create your views here.
import os

from django.contrib.sites.shortcuts import get_current_site
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class PDFhandle(APIView):
    permission_classes = [AllowAny,]

    def get(self, request):
        # zip_file = open('media/files/contrat.pdf', 'r')
        path = ''.join(['http://', get_current_site(request).domain, '/media/files/contrat.pdf'])
        return Response(
            {'url': path}
        )
