from django.shortcuts import render, redirect
from .models import Entry
from django.db.models import Q
from .filters import EntryFilter
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                    DetailView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView
                                    )


def get_entry_queryset(query=None):
    queryset = []
    queries = query.split(" ") 

    for q in queries:
        entries = Entry.objects.filter(
            Q(title__icontains=q) |
            Q(text__icontains=q)
            ).distinct()
        

        for entry in entries:
            queryset.append(entry)

    return list(set(queryset))

class EntryListView(ListView):


    queryset = Entry.objects.all()
    template_name = 'entries/index.html' #app/model_viewtype.html
    context_object_name = 'entries'
    ordering = ['-date_posted'] # order by the latest entries



def home_screen_view(request):
    context = {}
    entries = Entry.objects.all().order_by('-date_posted')

    searchFilter = EntryFilter(request.GET, queryset=entries)
    filteredEntries = searchFilter.qs
    


    context= {
        'entries': filteredEntries,
        'searchFilter': searchFilter
    }

    return render(request, 'entries/index.html', context)





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


