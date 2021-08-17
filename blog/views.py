
from blog.models import Post
from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import send_mail, get_connection

def contact(request):
    submitted = False
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #assert False 
            send_mail(
                cd['tema'],
                cd['cuerpo'],
                cd.get('email', 'noreply@example.com'),
                ['pieroramirez810@gmail.com'],
                connection=get_connection('django.core.mail.backends.console.EmailBackend')
            )
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted=True

    return render(request, 'contact.html', {'form': form, 'submitted': submitted})



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

