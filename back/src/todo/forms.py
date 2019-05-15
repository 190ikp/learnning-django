from django import forms
from .models import Post
import bootstrap_datepicker_plus as datetimepicker

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'deadline', 'when_remind',)
        widgets = {
            'deadline': datetimepicker.DateTimePickerInput(
                format='%Y-%m-%d %H:%M:%S',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                    'ignoreReadonly': True,
                    'allowInputToggle': True,
                }
            )
        }