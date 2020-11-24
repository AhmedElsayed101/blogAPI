from django.urls import path
from posts import views

urlpatterns = [
    path('<int:pk>/', views.postDetail.as_view()),
    path('', views.PostList.as_view())
]