from rest_framework.serializers import ModelSerializer
from users.models import Candidate, Collaborator, Accountant, AccountType, PhysicPerson, MoralPerson


class AccountantSerializer(ModelSerializer):
    class Meta:
        model = Accountant
        fields = ('id', 'account', 'denomination_social', 'nom_representant', 'lordre_numero', 'tableau_inscrit'
                  'address', 'code_postale', 'ville', 'phone', 'commentaire')


class AccountTypeSerializer(ModelSerializer):
    # account = AccountSerializer()

    class Meta:
        model = AccountType
        fields = ('id', 'account', 'type')


class CollaboratorSerializer(ModelSerializer):
    # account = AccountSerializer()
    # accountant = AccountantSerializer()

    class Meta:
        model = Collaborator
        fields = ('id', 'account', 'accountant')

    def create(self, validated_data):
        collaborator = Collaborator.objects.create(**validated_data)
        AccountType.objects.create(account=collaborator.account, type='Collaborateur')
        return collaborator


class CandidateSerializers(ModelSerializer):
    # account = AccountSerializer(read_only=True)
    # collaborator = CollaboratorSerializer(read_only=True)

    class Meta:
        model = Candidate
        fields = ('id', 'account', 'collaborator', 'birth_date', 'city_birth', 'department_birth',
                  'country_birth', 'address', 'additional_address', 'zip_code', 'city_address')

    def create(self, validated_data):
        candidate = Candidate.objects.create(**validated_data)
        AccountType.objects.create(account=candidate.account, type='Candidat')
        return candidate


class PhysicPersonSerializer(ModelSerializer):
    # account = AccountSerializer(read_only=True)

    class Meta:
        model = PhysicPerson
        fields = ('id', 'account', 'birth_date', 'city_birth', 'department_birth', 'country_birth',
                  'address', 'additional_address', 'zip_code', 'city_address')

    def create(self, validated_data):
        physic_person = PhysicPerson.objects.create(**validated_data)
        AccountType.objects.create(account=physic_person.account, type='Mandataire Physique')
        return physic_person


class MoralPersonSerializer(ModelSerializer):
    # account = AccountSerializer(read_only=True)

    class Meta:
        model = MoralPerson
        fields = ('id', 'account', 'association_name', 'address', 'additional_address',
                  'zip_code', 'city_address', 'national_number')

    def create(self, validated_data):
        physic_moral = PhysicPerson.objects.create(**validated_data)
        AccountType.objects.create(account=physic_moral.account, type='Mandataire Morale')
        return physic_moral
