from django import forms

class Contacto(forms.Form):
    nombre = forms.CharField(max_length=20, required=True)
    correo = forms.EmailField(required=True)