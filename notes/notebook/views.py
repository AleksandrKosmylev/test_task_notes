from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from notebook.models import Notes
from notebook.serializers import NotesSerializer


@csrf_exempt
def snippet_list(request):
    """
    List all code notes, or create a new note.
    """
    if request.method == 'GET':
        list_notes = Notes.objects.all()
        serializer = NotesSerializer(list_notes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NotesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)