from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from notebook.models import Notes
from notebook.serializers import NotesSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions

"""
@api_view(['GET', 'POST'])
def notes_list(request):

    if request.method == 'GET':
        list_notes = Notes.objects.all()
        serializer = NotesSerializer(list_notes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""


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