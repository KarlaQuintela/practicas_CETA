from django import forms
from .module_user.models import Role

class RoleForm(forms.ModelForm):

    class Meta:
        model = Role
        fields = [
            'name_role',
            'description_role',
        ]
        labels = {
            'name_role': 'Name_Role',
            'description_role': 'Description_role',
        }
        widgets = {
            'name_role': forms.TextInput(attrs={'class':'form-control'}),
            'description_role': forms.TextInput(attrs={'class':'form-control'}),
        }
