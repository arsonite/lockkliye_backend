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


class Server(RETRIEVE, UPDATE, DESTROY, GENERIC):
    def get(self, request, *args, **kwargs):
        data = json.loads(request.body)
        response = dict()
        return Response(response, status=status.HTTP_200_OK, content_type='application/json')
