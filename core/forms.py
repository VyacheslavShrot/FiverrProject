from django import forms
from django.core.exceptions import ValidationError
from phonenumber_field.formfields import PhoneNumberField


class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone_number = PhoneNumberField()
    country = forms.CharField(max_length=30)
    amount_people = forms.IntegerField()
    budget = forms.IntegerField()
    desc_project = forms.CharField(max_length=500)
    dead_line = forms.CharField()
    img = forms.ImageField(required=False)
    title_of_doc = forms.CharField(max_length=50)
    screen_play = forms.CharField(max_length=500)

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]

        if len(phone_number) != 12:
            raise ValidationError("Example +12345678900!!!")

        return phone_number


