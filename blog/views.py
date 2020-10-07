from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import CommentForm, UserBlogForm, EditPost
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    template = 'blog/list.html',
    context = {
        'page': page,
        'posts': posts,
        }

    return render(request, template, context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status='published', slug=post,
                             publish__year=year, publish__month=month,
                             publish__day=day)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
        try:
            profile = UserProfile.objects.get(user=request.user)
            comment_form = CommentForm(initial={
                'name': profile.user,
                'email': profile.user.email,
            })
        except UserProfile.DoesNotExist:
            comment_form = CommentForm()
    template = 'blog/detail.html',
    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        }

    return render(request, template, context)


@login_required
def post_publish(request, year, month, day, post):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    post = get_object_or_404(Post, status='draft', slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    if request.method == 'POST':

        edit_post = EditPost(data=request.POST)
        if edit_post.is_valid():
            post.status = request.POST.get("status")
            post.save()
            return redirect(reverse('blog:draft_list'))
    else:
        edit_post = EditPost()

    template = 'blog/draft_detail.html',
    context = {
        'post': post,
        'edit_post': edit_post,
        }

    return render(request, template, context)


@login_required
def add_blog_entry(request):
    """ Add a blog  """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = UserBlogForm(request.POST)

        if form.is_valid():
            blog_entry = form.save(commit=False)
            blog_entry.author = request.user
            blog_entry.save()
            messages.success(request, 'Successfully added BLOG!')
            return redirect(reverse('blog:add_blog_entry'))
        else:
            messages.error(request, 'Failed to add blog. Please ensure the form is valid.')
    else:
        form = UserBlogForm(initial={'author': request.user})

    template = 'blog/add_blog.html'
    context = {
        'form': form,
        }

    return render(request, template, context)


@login_required
def draft_list(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    object_list = Post.draft.all()
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    template = 'blog/drafts.html'
    context = {
        'page': page,
        'posts': posts,
        }

    return render(request, template, context)
