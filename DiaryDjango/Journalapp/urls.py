from django.urls import path
from . import views

urlpatterns = [
  path('', views.JournalListView.as_view(), name="journallist"),
  path('journal/journalcreate', views.JournalCreateView.as_view(),  name="createjournal"),
]