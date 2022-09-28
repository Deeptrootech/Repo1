from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Student


# Create your views here.
class StudentCreateView(CreateView):
    model = Student
    template_name = "student_create.html"
    fields = ["Title", "Description"]
    success_url = "/"

# Retrieve Views
class StudentListView(ListView):
    model = Student
    # queryset = Student.objects.all()
    template_name = "student_list.html"


class StudentDetailView(DetailView):
    model = Student
    # queryset = Student.objects.all()[:1]
    template_name = "student_detail.html"


# UpdateView
class StudentUpdateView(UpdateView):
    model = Student
    template_name = "student_update.html"
    fields = ["Title", "Description"]
    success_url = "/"


# DeleteView
class StudentDeleteView(DeleteView):
    model = Student
    template_name = "student_confirm_delete.html"
    success_url = "/"
