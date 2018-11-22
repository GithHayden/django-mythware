from django import forms
from .models import Post

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'published_date', 'author', 'issue_type', 'amount_paid', 'status', 'details')