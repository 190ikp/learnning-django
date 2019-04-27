from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title',)
        widgets = {
            'title': forms.Textarea(attrs={'cols': 20, 'rows': 1}),
        }