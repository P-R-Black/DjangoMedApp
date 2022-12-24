from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    date_of_birth = forms.DateField()

    class Meta:
        model = User
        fields = ['username', 'email', 'date_of_birth', 'password1', 'password2']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['email'].widget.attrs.update({"placeholder": "Email"})