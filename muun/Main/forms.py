from django import forms


class UserForm(forms.Form):
    class Meta:
        fields = ['username', 'password']