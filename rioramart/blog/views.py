from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.

def blog(request):
    post = Post.objects.all()
    context = {
        'posts': post
    } 
    return render(request, 'blog/blog.html', context=context)

def blog_single(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    post.views += 1
    post.save(update_fields=['views'])
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:blog_single', slug=post.slug)
    
    else:
        form = CommentForm()
    
    comment = Comment.objects.filter(post=post)
    context = {
        'posts': post,
        'comments': comment,
        'form': form
    }
    return render(request, 'blog/blog-single.html', context=context)
