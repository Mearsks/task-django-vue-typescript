from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserList.as_view()),
    path('create-users/', UserCreate.as_view()),
    path('users/<pk>/', UserRetrieveUpdate.as_view()),

    path('pilecolors/', PileColorListCreate.as_view()),
    path('pilecolors/<pk>/', PileColorRetrieveUpdate.as_view()),

    path('Task/', TaskListCreate.as_view()),
    path('Task/<pk>/', TaskRetrieveUpdate.as_view()),

    path('comments/', CommentListCreate.as_view()),
    path('comments/<pk>/', CommentRetrieveUpdate.as_view())
]