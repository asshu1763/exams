from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy
from . import models

# Create your views here.
class IndexView(TemplateView):
    template_name = 'basic_app/index.html'

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class SchoolListViewSt(ListView):
    context_object_name = 'schoolst'
    model = models.SchoolSt

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolDetailViewSt(DetailView):
    context_object_name = 'schoolst_detail'
    model = models.SchoolSt
    template_name = 'basic_app/schoolst_detail.html'

class SchoolCreateView(CreateView):
    fields = ('ques', 'ans')
    model = models.School

class SchoolCreateViewSt(CreateView):
    fields = ('ques', 'ans')
    model = models.SchoolSt


class SchoolUpdateView(UpdateView):
    fields = ('ques', 'ans')
    model = models.School

class SchoolUpdateViewSt(UpdateView):
    fields = ('ques', 'ans')
    model = models.SchoolSt

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')

class SchoolDeleteViewSt(DeleteView):
    model = models.SchoolSt
    success_url = reverse_lazy('basic_app:list_st')
