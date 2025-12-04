from django.db import models
from django.utils import timezone
from django.conf import settings # Para importar o modelo de User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

# --- NOVO MODELO ---
class Comment(models.Model):
    # Relacionamento com o Post (um post tem muitos comentários)
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    
    # Relacionamento com o Usuário (autor)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    text = models.TextField(verbose_name="Comentário")
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text