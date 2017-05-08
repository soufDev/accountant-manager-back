from django.contrib.auth.decorators import permission_required
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.api.serializer import AccountSerializer
from authentication.models import Account


class AuthRegister(APIView):
    serializer_class = AccountSerializer
    permission_classes = [AllowAny,]

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def account_list(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)
