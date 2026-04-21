from django import forms 
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'text', )
        widgets = {
            'text': forms.TextInput(attrs={'class': 'position-relative mb-4 w-100 overflow-hidden rounded-lg bg-white pr-3',
                                                'placeholder': 'Comment'})
        }