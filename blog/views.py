from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

# 1. Listar (ListView)
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts' # O nome da variável no HTML
    ordering = ['-date'] # Ordem decrescente de data

# 2. Detalhes (DetailView) - Já trata o erro 404 automaticamente!
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# 3. Criar (CreateView)
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list') # Para onde ir depois de salvar?

# 4. Atualizar (UpdateView)
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    # Redireciona para o detalhe do post editado
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

# 5. Deletar (DeleteView)
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post_list')