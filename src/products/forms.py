from django import forms

from .models import Product

class ProductFrom(forms.ModelForm):
    title = forms.CharField(required=True )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder':"Enter Desc",
                "class": "my_new two",
                "id": "my_text_area",
                "rows":10,
                "columns":10
            }
        )
    )
    email = forms.EmailField()
    price = forms.DecimalField(initial=199.33)

    class Meta:
        model = Product
        fields = [
            'title', 'description', 'price', 'email'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("Not a Valid Title")
        # if not "AMY" in title:
        #     raise forms.ValidationError("Not a Valid Title")
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("Not a Valid Email")
        return email

class RawProductForm(forms.Form):
    title = forms.CharField(required=True )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder':"Enter Desc",
                "class": "my_new two",
                "id": "my_text_area",
                "rows":10,
                "columns":10
            }
        )
    )
    price = forms.DecimalField(initial=199.33)