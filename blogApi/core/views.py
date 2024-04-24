from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from core.models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import permissions


class PostList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    """
    List all Posts, or create a new Post.
    """
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PostAPIViews(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    """
    Retrieve, update or delete a Post instance.
    """
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

