from blog.views import BlogDeleteView, BlogDetailView, BlogListView, BlogCreateView, BlogUpdateView, contact
from django.urls import path

urlpatterns=[
    path('',BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name="detail"),
    path('post/new/',BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit' ),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name="post_delete"),
    path('contact/',contact, name='contact'),
    
]
