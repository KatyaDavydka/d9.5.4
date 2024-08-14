from datetime import date
from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'author', 'category', 'title', 'text'}


    def clean(self):
        cleaned_data = super().clean()
        author = cleaned_data.get('author')
        today = date.today()
        post_limit = Post.objects.filter(author=author, post_time__date=today).count()
        if post_limit >= 3:
            raise ValidationError('Нельзя публиковать больше трех новостей в сутки!')
        return cleaned_data