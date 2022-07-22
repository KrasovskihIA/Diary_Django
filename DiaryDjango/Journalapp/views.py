from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Journal
from django.views.generic import ListView, CreateView
from .forms import JournalForm


class JournalListView(ListView):
    model = Journal
    template_name = "journal/journal_list.html"
    context_object_name = "journal_list"


class JournalCreateView(CreateView):    
    model = Journal
    form_class = JournalForm
    template_name = 'journal/create_journal_form.html'
    success_url = reverse_lazy('journallist')