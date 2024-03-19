from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from .models import Comment, Post, Reply
from account.models import User
from .serializers import CommentSerializer, PostSerializer, ReplySerializer
from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# API Views COMMENT
@swagger_auto_schema(
    method='POST',
    request_body=CommentSerializer,
    responses={201: 'CREATED', 400: 'Bad Request'}
)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comment_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comment_detail(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# API Views POST
@swagger_auto_schema(
    method='POST',
    request_body=PostSerializer,
    responses={201: 'CREATED', 400: 'Bad Request'}
)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# API Views REPLY
@swagger_auto_schema(
    method='POST',
    request_body=ReplySerializer,
    responses={201: 'CREATED', 400: 'Bad Request'}
)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def reply_list(request):
    if request.method == 'GET':
        replies = Reply.objects.all()
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# -------------------Tag List ---------------------
# @swagger_auto_schema(
#     method='POST'
# )
# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def tagged(request, pk):
#     if request.method == 'GET':
#         # Retrieve all tags
#         tags = Post.objects.all()
#         serializer = TagSerializer(tags, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = TagSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

