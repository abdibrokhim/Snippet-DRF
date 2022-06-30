from django.contrib import admin
from django.urls import path, include
from snippets import views

urlpatterns = [
    path('list/', views.SnippetList.as_view()),
    path('list/<int:pk>', views.SnippetDetail.as_view()),

]