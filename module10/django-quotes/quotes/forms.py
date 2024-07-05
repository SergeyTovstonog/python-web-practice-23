from django import forms

from quotes.models import Tag, Authors, Quote


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Authors
        fields = ['name', 'bio']

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'author', 'tags']
        widgets = {
            'tag': forms.CheckboxSelectMultiple()
        }