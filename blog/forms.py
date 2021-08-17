from django import forms

class ContactForm(forms.Form):
    nombre=forms.CharField(max_length=20, required=True, label="Nombre") 
    email=forms.EmailField(required=True, label="Correo")
    tema=forms.CharField(max_length=50)
    cuerpo=forms.CharField(widget=forms.Textarea)