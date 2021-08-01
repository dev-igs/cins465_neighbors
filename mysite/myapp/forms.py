from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label = "Email",
        required=True,
    )
    #meta class defined the model as tuple
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2"
        )
    
    def save(self, commit = True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
