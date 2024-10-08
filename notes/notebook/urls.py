from django.urls import path, include
from notebook import views

urlpatterns = [
    path('', views.main),
    path('notes/', views.NotesList.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
