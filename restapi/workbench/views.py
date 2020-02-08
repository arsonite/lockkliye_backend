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


class Workbenches(LIST, CREATE, GENERIC):
    """
        REST-API for 'Workbench'-collection
    """

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        response = {}
        return Response(status=status.HTTP_200_OK, content_type='application/json')

    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        response = {}
        return Response(json.loads(response), status=status.HTTP_200_OK, content_type='application/json')


class Workbench(RETRIEVE, UPDATE, DESTROY, GENERIC):
    """
        REST-API for single 'Workbench'-instances
    """

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        response = {}
        return Response(response, status=status.HTTP_200_OK, content_type='application/json')
