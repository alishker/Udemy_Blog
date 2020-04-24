from django.urls import path
from blog.views import AboutView

urlpatterns = [
    path("", postListView.as_view(), name="post"),
    path("about/", AboutView.as_view(), name="about"),
    path("posts/<int:pk>/$", views.PostDetailView.as_view(), name="post_detail"),
]
