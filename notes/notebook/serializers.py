from rest_framework import serializers
from notebook.models import Notes
from django.contrib.auth.models import User


class NotesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Notes
        fields = ['id','owner', 'title', 'note_body']

    def create(self, validated_data):
        """
        Create and return a new `Note` instance, given the validated data.
        """
        return Notes.objects.create(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(many=True, queryset=Notes.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'notes']
        