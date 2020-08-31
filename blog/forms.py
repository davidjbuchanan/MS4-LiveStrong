from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class UserBlogForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('publish', 'created', 'updated', 'slug', 'status') #new author removed

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'body': 'Body',
            'author': 'Author' #new
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        self.fields['author'].disabled = True  #new
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = True  #new
