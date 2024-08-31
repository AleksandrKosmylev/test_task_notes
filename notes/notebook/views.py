from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from notebook.models import Notes
from notebook.serializers import NotesSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from django.http import HttpResponse

def main(request):
    return HttpResponse(
        '<p>Hello Tests_task! Check notes/</p>'
                        )  


class NotesList(generics.ListCreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer