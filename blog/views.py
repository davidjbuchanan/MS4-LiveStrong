from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import CommentForm, UserBlogForm


def post_list(request):
    # posts = Post.published.all()
    object_list = Post.published.all()
    paginator = Paginator(object_list, 6)  # 6 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:  # If page is not an integer deliver the 1st page
        posts = paginator.page(1)
    except EmptyPage:  # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/list.html',
                  {'page': page,
                   'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    template = 'blog/detail.html',
    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
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
    else:  # it is a GET request
        form = UserBlogForm(initial={'author': request.user})  # new

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


# new beneath this line
def draft_list(request):
    object_list = Post.draft.all()
    paginator = Paginator(object_list, 6)  # 6 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:  # If page is not an integer deliver the 1st page
        posts = paginator.page(1)
    except EmptyPage:  # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    template = 'blog/drafts.html'
    context = {
        'page': page,
        'posts': posts
    }
    return render(request, template, context)
