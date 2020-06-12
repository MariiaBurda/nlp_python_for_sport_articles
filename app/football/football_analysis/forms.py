from django import forms


class ArticleForm(forms.Form):
    input_text = forms.CharField(label='', widget=forms.Textarea(attrs={"rows": 20, "cols": 110}))
