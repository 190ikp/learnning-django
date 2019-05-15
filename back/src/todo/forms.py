from django import forms
from .models import Post

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('title', 'content', 'deadline', 'when_remind',)

class PostForm(forms.Form):
    title = forms.CharField(
        label='タイトル',
        max_length=20,
        required=True,
    )
    
    content = forms.Textarea(
        label='内容',
        widget=forms.TextInput(),
        required=True,
    )

    deadline = forms.DateTimeField(
        label='期限',
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        input_formats=['%Y-%m-%dT%H:%M'],
        required=True,
    )

    when_remind = forms.ChoiceField(
        label='通知',
        widget=forms.Select,
        choices=Post.WHEN_REMIND,
        required=True,
    )