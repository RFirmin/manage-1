from django import forms

from .models import Category, Equipment, Equipment_Out

from django.contrib.auth.forms import UserCreationForm


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', 'description', 'image')

    choices_c = [("routeur", "Routeur"), ("cable", "Cable"), ("pc", "Pc"), ("switch", "Switch")]
    title = forms.ChoiceField(choices = choices_c, widget=forms.Select(attrs={
        'class': 'form-control',
    }))
    description = forms.CharField(required=False, widget=forms.Textarea)
    image = forms.ImageField(required=False, widget=forms.ClearableFileInput)


class EquipmentForm(forms.ModelForm):
    class Meta: 
        model = Equipment
        fields = ('serialNumber', 'description', 'supplier', 'cost', 'classed',)

    serialNumber = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    })) 
    supplier = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    cost = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
    }))
    classed = forms.ModelChoiceField(queryset=Category.objects.all(), label ="Category", widget=forms.Select)

    labels = {
        "classed": "Category",
    }


class EquipmentOutForm(forms.ModelForm):
    class Meta:
        model = Equipment_Out
        fields = ('serialNumber', 'description', 'supplier', 'classed')

    serialNumber = forms.ModelChoiceField(queryset=Equipment.objects.all(), widget=forms.Select)
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    supplier = forms.CharField(max_length=100)
    classed = forms.ModelChoiceField(queryset=Category.objects.all(), label ="Category", widget=forms.Select)
    



#

"""
class EquipmentOutForm(forms.ModelForm):
    class Meta: 
        model = Equipment_Out
        fields = ('serialNumber', 'description', 'projet', 'classed',)

    classed = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select)
    serialNumber = forms.ModelChoiceField(queryset=Equipment.objects.all(), widget=forms.Select)
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    })) 
    projet = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    labels = {
        "classed": "Category",
    }
"""

"""
class EquipmentOutForm(forms.Form):
    classed = forms.ModelChoiceField(queryset=Category.objects.all(), label = "Category"
        widget=forms.Select(attrs={"hx-get": "load_equipments/", "hx-target": "#id_serialNumber",
        'class': 'form-control'
    }))
    serialNumber = forms.ModelChoiceField(queryset=Equipment_Out.objects.none())
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    })) 
    projet = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)

        if "classed" in self.data:
            classed_id = int(self.data.get("classed"))
            self.fields["serialNumber"].queryset = Equipment_Out.objects.filter(classed_id=classed_id) 
"""