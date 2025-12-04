from django.contrib import admin
from .models import Post, Comment # Importe o Comment

admin.site.register(Post)
admin.site.register(Comment) # Registre aqui