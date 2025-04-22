from django import forms
from django.contrib.auth.models import User
from .models import Comment, Task

class TaskAssignForm(forms.ModelForm):
    assigned_to = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(is_superuser=False),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to','status', 'attachment', 'tags']

        
class TaskStatusForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['status']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Yorumunuzu yazın...'})
        }
