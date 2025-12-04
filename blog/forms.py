from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')

# --- NOVO FORM ---
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',) # Só pedimos o texto, o resto (autor, data, post) preenchemos automaticamente