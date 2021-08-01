from django import forms
from django.core.validators import validate_slug
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

from . import models

class ReplyForms(forms.Form):

    QUESTION1 = (
        (0, "Yes"),
        (1, "Not at all. They could be carried."),
    )
    QUESTION2 = (
        (0, "No"),
        (1, "It could grip it by the husk!"),
    )
    QUESTION3 = (
        (0, "Sure"),
        (1, "Well, it doesn't matter."),
    ) 

    question1 = forms.ChoiceField(
        label = "Question 1: Are you suggesting that coconuts migrate?",
        required = True,
        choices= QUESTION1,
        widget=forms.RadioSelect(),
        validators=[
            validate_slug
        ]
    )
    question2 = forms.ChoiceField(
        label = "Question 2: What? A swallow carrying a coconut?",
        required = True,
        choices= QUESTION2,
        widget=forms.RadioSelect(),
        validators=[
            validate_slug
        ]
    )
    question3 = forms.ChoiceField(
        label = "Question 3: It's not a question of where he grips it! It's a simple question of weight ratios! A five ounce bird could not carry a one pound coconut.",
        required = True,
        choices= QUESTION3,
        widget=forms.RadioSelect(),
        validators=[
            validate_slug
        ]
    )

    def save(self):
        reply_instance = models.FormsModel()
        reply_instance.reply1 = self.cleaned_data["question1"]
        reply_instance.reply2 = self.cleaned_data["question2"]
        reply_instance.reply3 = self.cleaned_data["question3"]
        reply_instance.save()
        return reply_instance



# REGISTRATION FORM, LOGIN, ACCOUNT
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        #validators=[must_be_unique]
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2"
        )
    
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user