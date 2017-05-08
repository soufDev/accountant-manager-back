from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from authentication.api.serializer import AccountSerializer
from users.api.serializers import CandidateSerializers, AccountTypeSerializer
from users.models import Candidate, AccountType


# Candidate Views
class CandidateList(generics.ListCreateAPIView):
    permission_classes = [AllowAny,]

    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializers


class CandidateDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny,]

    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializers


# Account type view
@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def profile_type(request, pk):
    message = "Profile Account Not Found"
    try:
        profile = AccountType.objects.get(account=pk)
        serializer = AccountTypeSerializer(profile)
        # print('serializer.data: '+serializer.data)
        if profile:
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'error': message}, status=status.HTTP_404_NOT_FOUND)
    except AccountType.DoesNotExist:
        print('pk exception = ', pk)
        return Response({'error': message}, status=status.HTTP_404_NOT_FOUND)



