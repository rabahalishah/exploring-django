from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField()
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={"placeholder": "My Description",
               "class": "new-class-name",
               "rows": 20,
               "columns": 100
               }))
    price = forms.DecimalField()

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
        # Custom validations

    def cleaned_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "rabah" == title:
            raise forms.ValidationError("This is not a valid title")
        else:
            return title


# class RawProductFrom(forms.Form):
#     title = forms.CharField()
#     description = forms.CharField(required=False, widget=forms.Textarea(
#         attrs={"placeholder": "My Description",
#                "class": "new-class-name",
#                "rows": 20,
#                "columns": 100
#                }))
#     price = forms.DecimalField()
