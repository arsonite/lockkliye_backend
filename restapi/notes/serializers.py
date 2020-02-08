from rest_framework import serializers


class LabelSerializer(serializers.Serializer):
    id = serializers.CharField()
    color = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()


class ListSerializer(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField()
    labels = LabelSerializer()


class NoteSerializer(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField()
    content = serializers.CharField()
    labels = LabelSerializer()


class FolderSerializer(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField()
    #subfolders = FolderSerializer()
    notes = NoteSerializer()
    lists = ListSerializer()
