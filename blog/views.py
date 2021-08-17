from blog.forms import Contacto
from blog.models import Post
from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, FormView,
    DeleteView
)
from django.urls import reverse_lazy


class ContactView(FormView):
    form_class = Contacto
    initial = {'key': 'value'}
    template_name= 'contact.html'


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    

class BlogDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
class BlogCreateView(CreateView):
    model = Post
    template_name ="post_new.html"
    fields=["titulo", "descripcion", "autor", "cuerpo"]

class BlogUpdateView(UpdateView):
    model= Post
    template_name ="post_edit.html"
    fields = ["titulo", "descripcion", "cuerpo"]

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

