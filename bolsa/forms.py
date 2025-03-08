from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import (
PerfilUsuario,Accion
)

#######


class ContactFormForm(forms.Form):
    # debe contener los atributos necesarios para poder recibir los datos necesarios en el modelo ContactForm
    # contact_form_uuid no necesita ser declarado en el form
    customer_name = forms.CharField(max_length=64, label="Nombre")
    customer_email = forms.EmailField(label="Correo")
    message = forms.CharField(label="Mensaje")


class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

    def save(self, commit=True):
        # Primero guarda el usuario
        user = super().save(commit=False)
        # Asigna el password
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()  # Guarda el usuario

            # Crea el perfil asociado
            PerfilUsuario.objects.create(
                user=user,
            )

        return user


class UserUpdateForm(forms.ModelForm):
    # telefono = forms.CharField(max_length=15, required=False)
    # direccion = forms.CharField(max_length=150, required=False)
    # id_nacional = forms.CharField(max_length=20, required=True)
    # tipo_usuario = forms.ModelChoiceField(
    #    queryset=TipoUsuario.objects.all(),
    #    required=False,
    #    empty_label="Seleccione un tipo de usuario",
    # )
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            # 'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            #'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            #'id_nacional': forms.TextInput(attrs={'class': 'form-control'}),
            #'tipo_usuario': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PerfilUpdateForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ["saldo"]
        widgets = {
            "saldo": forms.TextInput(attrs={"class": "form-control"}),
        }

class AccionForm(forms.ModelForm):
    class Meta:
        model = Accion
        fields = ['simbolo', 'nombre_empresa', 'precio_actual', 'cambio_porcentual']

