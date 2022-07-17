from django.shortcuts import render, redirect

from .models import postModel
from .forms import postForm


def index(request):
    posts = postModel.objects.all()
    categories = postModel.objects.values('kategori').distinct()
    context = {
        'title': 'Blog',
        'header': 'halaman blog',
        'Post': posts,
        'Category': categories
    }
    return render(request, 'blog/index.html', context)


def contentList(request):
    posts = postModel.objects.all()
    context = {
        'title': 'Post | content',
        'header': 'Daftar Postingan',
        'listPost': posts
    }
    return render(request, 'blog/listContent.html', context)


def detail(request, slugInput):
    details = postModel.objects.get(slug=slugInput)
    context = {
        'title': 'Detail',
        'header': 'halaman detail',
        'detailPost': details,
    }
    return render(request, 'blog/detail.html', context)


def postCategory(request, categoryInput):
    posts = postModel.objects.filter(kategori=categoryInput)
    categories = postModel.objects.values('kategori').distinct()
    context = {
        'title': 'Kategori',
        'categories': '',
        'Post': posts,
        'Category': categories,
    }
    return render(request, 'blog/category.html', context)


def create(request):
    postForms = postForm(request.POST or None)
    if request.method == 'POST':
        if postForms.is_valid():
            postForms.save()

            return redirect('blog:list')

    context = {
        'title': 'Blog | Post',
        'header': 'Silahkan Buat Postingan Baru',
        'createPost': postForms
    }
    return render(request, 'blog/create.html', context)


def update(request, updateId):
    updatePost = postModel.objects.get(id=updateId)
    data = {
        'author': updatePost.author,
        'judul': updatePost.judul,
        'kategori': updatePost.kategori,
        'konten': updatePost.konten
    }
    postForms = postForm(request.POST or None,
                         initial=data, instance=updatePost)
    if request.method == 'POST':
        if postForms.is_valid():
            postForms.save()

            return redirect('blog:list')

    context = {
        'title': 'Post | Update',
        'header': 'Silahkan ubah konten',
        'createPost': postForms
    }
    return render(request, 'blog/create.html', context)


def delete(request, deleteId):
    postModel.objects.filter(id=deleteId).delete()
    return redirect('blog:list')
