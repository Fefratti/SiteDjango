from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Post

# 1. Listar (Read)
def post_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# 2. Detalhes (Read) com erro 404 manual
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404("Post não encontrado")
    return render(request, 'blog/post_detail.html', {'post': post})

# 3. Criar (Create) - Manualmente pegando dados do HTML
def post_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        # Cria e salva no banco
        Post.objects.create(title=title, content=content)
        return redirect('post_list')
    return render(request, 'blog/post_form.html')

# 4. Atualizar (Update) - Manualmente
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('post_detail', pk=post.pk)
    return render(request, 'blog/post_form.html', {'post': post})

# 5. Deletar (Delete) - Com confirmação
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})