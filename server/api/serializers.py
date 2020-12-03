from django.contrib.auth.models import User

from .models import PileColor, Task, Comment
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """User model"""

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'password', 'is_active', 'is_superuser')


class PileColorSerializer(serializers.ModelSerializer):
    """ PileColor model"""

    class Meta:
        model = PileColor
        fields = ('id', 'name', 'description')


class TaskSerializer(serializers.ModelSerializer):
    """ Task Model """

    class Meta:
        model = Task
        fields = ('id', 'name', 'pile_color', 'stars', 'description', 'created')


class CommentSerializer(serializers.ModelSerializer):
    """ Comment model """

    class Meta:
        model = Comment
        fields = ('id', 'user', 'hedgehog', 'comment', 'visible', 'created')
