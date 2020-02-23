import abc

from rest_framework import generics, mixins

# Mixins
RETRIEVE = mixins.RetrieveModelMixin
UPDATE = mixins.UpdateModelMixin
DESTROY = mixins.DestroyModelMixin
GENERIC = generics.GenericAPIView


class AbstractRessource(RETRIEVE, UPDATE, DESTROY, GENERIC):
    @abc.abstractmethod
    def get(self, request, *args, **kwargs):
        pass

    @abc.abstractmethod
    def put(self, request, *args, **kwargs):
        pass

    @abc.abstractmethod
    def delete(self, request, *args, **kwargs):
        pass

    @abc.abstractmethod
    def patch(self, request, *args, **kwargs):
        pass
