from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from quotes.forms import TagForm, AuthorForm, QuoteForm
from quotes.models import Quote, Authors, Tag


# Create your views here.

class HomeView(ListView):
    model = Quote
    template_name = 'home.html'
    context_object_name = 'quotes'

class AuthorListView(ListView):
    model = Authors
    template_name = 'quotes/authors.html'
    context_object_name = 'authors'


class AddTagView(LoginRequiredMixin, CreateView):
    login_url = "/users/login/"
    model = Tag
    template_name = "quotes/add_tag.html"
    success_url = reverse_lazy('home')
    form_class = TagForm

class AddAuthorView(LoginRequiredMixin, CreateView):
    login_url = "/users/login/"
    model = Authors
    template_name = "quotes/add_author.html"
    success_url = reverse_lazy('home')
    form_class = AuthorForm

class AddQuoteView(LoginRequiredMixin, CreateView):
    login_url = "/users/login/"
    model = Authors
    template_name = "quotes/add_quote.html"
    success_url = reverse_lazy('home')
    form_class = QuoteForm