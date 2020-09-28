from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import CommentForm, UserBlogForm, EditPost


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
    return render(request,
                  'blog/list.html',
                  {'page': page,
                   'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             publish__year=year,
                             publish__month=month,
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
    if request.method == 'POST':
        edit_post = EditPost(data=request.POST)
        if edit_post.is_valid():
            edit_post = edit_post.save(commit=False)
            edit_post.post = post
            edit_post.save()
    else:
        edit_post = EditPost()

    template = 'blog/detail.html',
    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'edit_post': edit_post
        }

    return render(request, template, context)


def post_detail(request, year, month, day, post):
    print ('aaaaaaaaaaa')
    post = get_object_or_404(Post, status='published', slug=post, publish__year=year, publish__month=month, publish__day=day)
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
    edit_post = EditPost()  # xxx
    template = 'blog/detail.html',
    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'edit_post': edit_post,
        }
    return render(request, template, context)


def post_publish(request, year, month, day, post):
    print('bbbbbbbbbbbbbbb')
    post = get_object_or_404(Post, status='draft', slug=post, publish__year=year, publish__month=month, publish__day=day)
    if request.method == 'POST':
        edit_post = EditPost(data=request.POST)
        if edit_post.is_valid():
            edit_post = edit_post.save(commit=False)
            edit_post.post = post
            edit_post.save()
    else:
        edit_post = EditPost()

    template = 'blog/draft_detail.html',
    context = {
        'post': post,
        'edit_post': edit_post,
        }

    return render(request, template, context)


def add_blog_entry(request):
    """ Add a blog  """
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


def draft_list(request):
    print("woman")
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
        'posts': posts
    }

    return render(request, template, context)
