import json
import pickle

from rest_framework import generics, mixins, status
from rest_framework.response import Response

# Mixins
LIST = mixins.ListModelMixin
CREATE = mixins.CreateModelMixin
GENERIC = generics.GenericAPIView
RETRIEVE = mixins.RetrieveModelMixin
UPDATE = mixins.UpdateModelMixin
DESTROY = mixins.DestroyModelMixin


class Notes(LIST, CREATE, GENERIC):
    """
        REST-API for 'Note'-collection
    """

    def get(self, request, *args, **kwargs):
        response = {}
        return Response(status=status.HTTP_200_OK, content_type='application/json')

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        response = dict()
        return Response(response, status=status.HTTP_200_OK, content_type='application/json')


class Note(RETRIEVE, UPDATE, DESTROY, GENERIC):
    """
        REST-API for single 'Note'-instances
    """

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        response = {}
        return Response(response, status=status.HTTP_200_OK, content_type='application/json')
