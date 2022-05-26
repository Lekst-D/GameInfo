from django import forms
 
class UserForm(forms.Form):
    Id = forms.IntegerField()