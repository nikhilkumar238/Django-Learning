
from django import forms

from .models import Article
class ArticleForm(forms.ModelForm):
    # title = forms.CharField(required=True )
    # desc = forms.CharField(
    #     required=False,
    #     widget=forms.Textarea(
    #         attrs={
    #             'placeholder':"Enter Desc",
    #             "class": "my_new two",
    #             "id": "my_text_area",
    #             "rows":10,
    #             "columns":10
    #         }
    #     )
    # )
    # date = forms.DateField()

    class Meta:
        model = Article
        fields = [
            'title', 'desc', 'date'
        ]

    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     if not "CFE" in title:
    #         raise forms.ValidationError("Not a Valid Title")
    #     # if not "AMY" in title:
    #     #     raise forms.ValidationError("Not a Valid Title")
    #     return title