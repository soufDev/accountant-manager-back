from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from authentication.models import Account


class AccountCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(AccountCreationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Account
        fields = ('email',)


class AccountChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(AccountChangeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Account
        fields = '__all__'
