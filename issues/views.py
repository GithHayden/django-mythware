from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm


def get_posts(request):
    """
    Create a view that will return a
    list of Issues that were published prior to'now'
    and render them to the 'issuestracker.html' template
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')
    return render(request, "issuestracker.html", {'posts': posts})


def post_detail(request, pk):
    """
    Create a view that return a single
    Issue(Post) object based on the post ID and
    render it to the 'issuedetails.html'
    template. Or return a 404 error if the
    issue is not found
    """
    post = get_object_or_404(Post, pk=pk)
    post.save()
    return render(request, "issuedetails.html", {'post': post})


def create_or_edit_post(request, pk=None):
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'issuesform.html', {'form': form})