from django.shortcuts import render, redirect
from .models import Entry
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                    DetailView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView
                                    )



class EntryListView(ListView):
    queryset = Entry.objects.all()
    template_name = 'entries/index.html' #app/model_viewtype.html
    context_object_name = 'entries'
    ordering = ['-date_posted'] # order by the latest entries
    

class EntryDetailView(DetailView):
    model = Entry

class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    fields = ['title','text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EntryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Entry
    fields = ['title','text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        entry = self.get_object()
        if self.request.user == entry.author:
            return True
        return False

class EntryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Entry
    success_url = "/"
    
    def test_func(self):
        entry = self.get_object()
        if self.request.user == entry.author:
            return True
        return False
