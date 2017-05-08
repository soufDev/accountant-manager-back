from rest_framework import serializers

from authentication.models import Account


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Account
        fields = ('id', 'email', 'username',
                  'first_name', 'last_name', 'password', 'confirm_password')

    # read_only_fields = ('date_created', 'date_modified')

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)

        if password and password == confirm_password:
            instance.set_password(password)

        instance.save()

        return instance

    def validate(self, data):
        """
        ensure the passwords are the same
        :param data: 
        :return: 
        """
        if data['password']:
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError('The passwords have to the be the same')
        return data
