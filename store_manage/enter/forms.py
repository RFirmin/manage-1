from django import forms

from .models import Category, Equipment

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', 'description', 'image')

    choices_c = [("routeur", "Routeur"), ("cable", "Cable"), ("pc", "Pc"), ("switch", "Switch")]
    title = forms.ChoiceField(choices = choices_c, widget=forms.Select(attrs={
        'class': 'form-control',
    }))
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(widget=forms.ClearableFileInput)


class EquipmentForm(forms.ModelForm):
    class Meta: 
        model = Equipment
        fields = ('serial_number', 'description', 'procurement', 'cost', 'created_on', 'classed')

    serial_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    })) 
    procurement = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    cost = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
    }))
    created_on = forms.SelectDateWidget(disabled=True)
    classed = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select)

    labels = {
        "classed": "Category",
    }