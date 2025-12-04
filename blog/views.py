from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Post
from .forms import PostForm  # <--- NOVA IMPORTAÇÃO AQUI

# 1. Listar (Não muda)
def post_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# 2. Detalhes (Não muda)
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404("Post não encontrado")
    return render(request, 'blog/post_detail.html', {'post': post})

# 3. Criar (ALTERADO PARA USAR FORM)
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

# 4. Atualizar (ALTERADO PARA USAR FORM)
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        # Preenchemos o form com os dados novos (POST) e dizemos quem estamos editando (instance)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        # Preenchemos o form com os dados atuais do post
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})

# 5. Deletar (Não muda na Versão 2)
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})