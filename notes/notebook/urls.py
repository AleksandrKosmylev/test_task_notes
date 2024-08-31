from django.urls import path
from notebook import views

urlpatterns = [
    path('notes/', views.notes_list),
]
