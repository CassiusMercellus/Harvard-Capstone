from django.urls import path, include
from . import views
from .views import authView, home

app_name = 'journal'

urlpatterns = [
 path("", home, name="home"),
 path("signup/", authView, name="authView"),
 path("accounts/", include("django.contrib.auth.urls")),
 path('create/', views.create_journal, name='create_journal'),
 path('delete/<int:journal_id>/', views.delete_journal, name='delete_journal'),
 path('edit/<int:journal_id>/', views.edit_journal, name='edit_journal'),
 path('view/<int:journal_id>/', views.view_journal, name='view_journal'),
]