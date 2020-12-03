from django.contrib.auth.models import User
from rest_framework import generics, permissions

from .models import PileColor, Task, Comment
from .serializers import UserSerializer, PileColorSerializer, TaskSerializer, CommentSerializer


class UserList(generics.ListAPIView):
    """ すべてのユーザーを一覧表示する"""
    queryset = User.objects.all().order_by('first_name')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserCreate(generics.CreateAPIView):
    """ 新しいユーザーを作成するためのビューです。POST リクエストのみ受け付けます。 """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class UserRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ ユーザーを取得したり、ユーザー情報を更新したりします。
    GET および PUT リクエストを受け付け、リクエストにはレコード ID を指定しなければなりません。 """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class PileColorListCreate(generics.ListCreateAPIView):
    """ PileColorsの一覧と作成 """
    queryset = PileColor.objects.all()
    serializer_class = PileColorSerializer
    permission_classes = (permissions.IsAuthenticated,)


class PileColorRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ PileColor情報の取得と更新 """
    queryset = PileColor.objects.all()
    serializer_class = PileColorSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TaskListCreate(generics.ListCreateAPIView):
    """タスクのリスト化と作成"""
    queryset = Task.objects.all().order_by('name')
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TaskRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """タスクの取得と更新"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CommentListCreate(generics.ListCreateAPIView):
    """ タスクのリスト化または作成 """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CommentRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ タスクのリスト化または作成 """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)
