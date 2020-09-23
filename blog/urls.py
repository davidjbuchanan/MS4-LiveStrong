from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
    path('add_entry/', views.add_blog_entry, name='add_blog_entry'),
    path('drafts/', views.draft_list, name='draft_list'),
]
