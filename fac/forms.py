from django import forms

from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=['nombres','apellidos','tipo', 'telefono', 'email', 'identificacion', 'direccion', 'estado']
        exclude=['um','fm', 'uc', 'fc']
        widget={'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean(self):
        try:
            sc = Cliente.objects.get(
                email=self.cleaned_data["email"]
            )

            if not self.instance.pk:
                print("Registro ya existe")
                raise forms.ValidationError("Registro Ya Existe")
            elif self.instance.pk!=sc.pk:
                print("Cambio no permitido")
                raise forms.ValidationError("Cambio No Permitido")
        except Cliente.DoesNotExist:
            pass
        return self.cleaned_data