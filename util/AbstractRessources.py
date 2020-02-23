import abc

from rest_framework import generics, mixins

# Mixins
LIST = mixins.ListModelMixin
CREATE = mixins.CreateModelMixin
GENERIC = generics.GenericAPIView


class AbstractRessources(LIST, CREATE, GENERIC):
    @abc.abstractmethod
    def get(self, request, *args, **kwargs):
        pass

    @abc.abstractmethod
    def post(self, request, *args, **kwargs):
        pass
