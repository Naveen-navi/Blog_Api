from django.urls import path
from .views import * 
from . import views

# urlpatterns = [
    # path('posts/', PostList.as_view(),name='posts'),
    # path('posts1/', PostList1.as_view(),name='posts1'),
    # path('posts/<int:pk>/', PostDetail.as_view(),name='postdetail'),
    # path('posts/self/', PostListSelf.as_view(),name='postsearch'),
    # path('comments/', CommentList.as_view(),name='comments'),
    # path('comments/<int:pk>/', CommentDetail.as_view(),name='commentdetail'),
    # path('reply/', ReplyList.as_view(),name='replies'),
    # path('reply/self/', ReplyListSelf.as_view(),name='replysearch'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    # API Views COMMENT
    path('comments/', views.comment_list, name='comment-list'),
    path('comments/<int:pk>/', views.comment_detail, name='comment-detail'),

    # API Views POST
    path('posts/', views.post_list, name='post-list'),
    path('posts/<int:pk>/', views.post_detail, name='post-detail'),

    # API Views REPLY
    path('replies/', views.reply_list, name='reply-list'),

    # path('tagged/<int:pk>/', views.tagged, name='tagged'),

    #API views Likes
    # path('like_post/',views.like_post),
    # path('remove_like_post/',views.remove_like_post),
]

