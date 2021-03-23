from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Person

class PersonListView(ListView):
    template_name = 'djangox_app/person_list.html'
    model = Person

class PersonDetailView(DetailView):
    template_name = 'djangox_app/person_detail.html'
    model = Person

class PersonCreateView(CreateView):
    template_name = 'djangox_app/person_create.html'
    model = Person
    fields = ['name', 'description', 'profile_manager']
    success_url = reverse_lazy('person_list')

class PersonUpdateView(UpdateView):
    template_name = 'djangox_app/person_update.html'
    model = Person
    fields = ['name', 'description', 'profile_manager']
    success_url = reverse_lazy('person_list')

class PersonDeleteView(DeleteView):
    template_name = 'djangox_app/person_delete.html'
    model = Person
    success_url = reverse_lazy('person_list')
# Create your views here.
