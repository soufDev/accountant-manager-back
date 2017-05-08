from rest_framework import serializers

from contract.models import Contract


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        Model = Contract
        fields = ('id', 'file')
