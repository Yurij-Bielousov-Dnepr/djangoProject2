from django import forms
from django.utils.translation import gettext_lazy as _

class AddEmailForm(forms.Form):
    email = forms.EmailField(label=_('Email address'))

class RemoveEmailForm(forms.Form):
    email = forms.EmailField(label=_('Email address to remove'))
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Visitor

class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['userNick', 'category', 'district', 'languages', 'is_sponsor', 'phone_number', 'email', 'favorites']
        widgets = {
            'district': forms.CheckboxSelectMultiple(),
            'languages': forms.CheckboxSelectMultiple(),
            'favorites': forms.SelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))