from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, PostCadastro
from .forms import PostForm, PostCadastroForm
from django.shortcuts import redirect
from django.utils.timezone import localdate
from datetime import datetime
from events.models import Event


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    day = datetime(localdate().year, localdate().month, localdate().day)
    context = {

        'events': Event.objects.filter(
            date='{:%Y-%m-%d}'.format(day)).order_by('-priority', 'event'),
        'form': form
    }

    return render(request, 'blog/post_edit.html', context)

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    day = datetime(localdate().year, localdate().month, localdate().day)
    context = {

         'events': Event.objects.filter(
                date='{:%Y-%m-%d}'.format(day)).order_by('-priority', 'event'),
        'form': form
    }
    return render(request, 'blog/post_edit.html', context)

def post_draft_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def post_cadastro(request):
    posts = PostCadastro.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_cadastro.html', {'posts': posts})



def post_newcadastro(request):
    if request.method == "POST":
        form = PostCadastroForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detailcadastro', pk=post.pk)
    else:
        form = PostCadastroForm()
        return render(request, 'blog/post_newcadastro.html', {'form': form})

def post_detailcadastro(request, pk):
    post = get_object_or_404(PostCadastro, pk=pk)
    return render(request, 'blog/post_detailcadastro.html', {'post': post})


def post_editcadastro(request, pk):
    post = get_object_or_404(PostCadastro, pk=pk)
    if request.method == "POST":
        form = PostCadastroForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detailcadastro', pk=post.pk)
    else:
        form = PostCadastroForm(instance=post)
    return render(request, 'blog/post_newcadastro.html', {'form': form})
