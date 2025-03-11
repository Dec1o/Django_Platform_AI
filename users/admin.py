from django.contrib import admin
from .models import User
from django import forms

class UserAdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ('name', 'email', 'password', 'company')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Define a senha de forma segura
        if commit:
            user.save()
        return user

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm
    list_display = ('name', 'email', 'company', 'data_criacao')
    fields = ('name', 'email', 'password', 'company')
