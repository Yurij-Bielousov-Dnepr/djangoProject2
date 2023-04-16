# views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# from .forms import ArticleForm, EventForm, HelperForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# from helpy.forms import EventForm, ArticleForm
# from helpy.models import Article, Event, Helper
#
#
# # Классы-представления для статей (Article)
# class ArticleListView(ListView):
#     model = Article
#     template_name = 'helpy/event_article/articles.html'
#     context_object_name = 'articles'
#
#
# # class ArticleDetailView(DetailView):
# #     model = Article
# #     template_name = 'article_detail.html'
# #     context_object_name = 'article'
#
# class ArticleCreateView(CreateView):
#     model = Article
#     template_name = 'helpy/event_article/add_article.html'
#     fields = ('article_name', 'article_text', 'article_tags', 'username',)
#     success_url = reverse_lazy('article')
#
#
# class ArticleUpdateView(UpdateView):
#     model = Article
#     template_name = 'article_form.html'
#     fields = ('title', 'content',)
#     success_url = reverse_lazy('article_list')
#
#
# # class ArticleDeleteView(DeleteView):
# #     model = Article
# #     template_name = 'article_confirm_delete.html'
# #     success_url = reverse_lazy('article_list')
#
#
# # Классы-представления для мероприятий (Event)
# # class EventListView(ListView):
# #     model = Event
# #     template_name = 'event_list.html'
# #     context_object_name = 'events'
#
# class Events(DetailView):
#     model = Event
#     template_name = 'helpy/event_article/events.html'
#     context_object_name = 'event'
#
#
# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['events'] = Event.objects.all()
#     return context
#
#
# class EventCreateView(CreateView):
#     model = Event
#     template_name = 'helpy/event_article/add_event.html'
#     fields = ('Calendar', 'Events Calendar', 'Google Maps',)
#     success_url = reverse_lazy('events')
#
#
# class EventUpdateView(UpdateView):
#     model = Event
#     template_name = 'event_form.html'
#     fields = ('name', 'description', 'date',)
#     success_url = reverse_lazy('event_list')
#
#
# class EventDeleteView(DeleteView):
#     model = Event
#     template_name = 'event_confirm_delete.html'
#     success_url = reverse_lazy('events')
#
#
# # Классы-представления для помощников (Helper)
# # class HelperListView(ListView):
# #     model = Helper
# #     template_name = 'helper_list.html'
# #     context_object_name = 'helpers'
# #
# #
# # class HelperDetailView(DetailView):
# #     model = Helper
# #     template_name = 'helper_detail.html'
# #     context_object_name = 'helper'
#
#
# # class HelperCreateView(CreateView):
# #     model = Helper
# #     template_name = 'helper_form.html'
# #     fields = ('name', 'email', 'phone',)
# #     success_url = reverse_lazy('helper_list')
#
#
# class HelperUpdateView(UpdateView):
#     model = Helper
#     template_name = 'helper_form.html'
#     fields = ('name', 'email', 'phone',)
#     success_url = reverse_lazy('helper_list')
#
# def add_article(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             article = form.save()
#             return redirect('article_detail', pk=article.pk)
#     else:
#         form = ArticleForm()
#     return render( request, 'helpy/event_article/add_article.html', {'form': form} )
#
#
# def add_event(request):
#     if request.method == 'POST':
#         form = EventForm(request.POST)
#         if form.is_valid():
#             event = form.save()
#             return redirect('event_detail', pk=event.pk)
#     else:
#         form = EventForm()
#     return render( request, 'helpy/event_article/add_event.html', {'form': form} )
#
#
# def add_helper(request):
#     if request.method == 'POST':
#         form = HelperForm(request.POST)
#         if form.is_valid():
#             helper = form.save()
#             return redirect('helper_detail', pk=helper.pk)
#     else:
#         form = HelperForm()
#     return render( request, 'helpy/add_helper.html', {'form': form} )
#
# def events(request):
#     events = Event.objects.order_by('date')[:3]
#     context = {
#         'events': events
#     }
#     return render( request, 'helpy/event_article/events.html', context )
#
# def index(request):
#     return render( request, 'helpy/index.html' )
#
# def articles(request):
#     return render( request, 'helpy/event_article/articles.html' )
#
#
# def events(request):
#     return render( request, 'helpy/event_article/events.html' )
#
#
# def about(request):
#     return render( request, 'helpy/about.html' )
#
#
# def login(request):
#     return render( request, 'helpy/templates/account/sign_in.html' )
#
#
# class ArticleFormView:
#     def get(self, request, *args, **kwargs):
#         return render( request, 'helpy/event_article/articles.html' )
#
#
# class ArticleDetailView:
#     pass
