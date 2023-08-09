from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Student
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from .forms import EditForm
from django.urls import reverse_lazy


# Create your views here.
def HomePage(request):
    return render(request, 'home.html')

class StudentPage(ListView):
    model=Student
    template_name = 'student.html'
    context_object_name = 'students'
class DetailPage(DetailView):
    model = Student
    template_name = 'detail.html'
    context_object_name = 'detail'

class EditPage(UpdateView):
    model=Student
    template_name = 'edit.html'
    form_class = EditForm
    success_url = reverse_lazy('home')

class DeletePage(DeleteView):
    model=Student
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
class CreatePage(CreateView):
    model=Student
    template_name = 'create.html'
    form_class = EditForm
    success_url = reverse_lazy('home')