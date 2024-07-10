
from core.fabrica_histologia.serializers import SystemDetailSerializer, SystemWriteSerializer, PointDetailSerializer, PointWriteSerializer


from core.fabrica_histologia.serializers import SystemDetailSerializer, SystemWriteSerializer, speciesDetailSerializer, speciesWriteSerializer
from core.fabrica_histologia.models import System, Species
from core.fabrica_histologia.serializers import SlideMicroscopyPostDetailSerializer, SlideMicroscopyPostListSerializer, SlideMicroscopyPostWriteSerializer, SystemDetailSerializer, SystemWriteSerializer
from core.fabrica_histologia.models import SlideMicroscopyPost, System

from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema

# Create your views here.

#System view

@extend_schema(tags=["System"])
class SystemViewSet(ModelViewSet):
    queryset = System.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return SystemDetailSerializer
        return SystemWriteSerializer
    http_method_names = ["get", "post", "put", "delete"]

class PointViewSet(ModelViewSet):
    queryset = Points.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return PointDetailSerializer
        return PointWriteSerializer
    http_method_names = ["get", "post", "put", "delete"]

@extend_schema(tags=["Species"])
class SpeciesViewSet(ModelViewSet):
    queryset = Species.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return speciesDetailSerializer
        return speciesWriteSerializer
    http_method_names = ["get", "post", "put", "delete"]

@extend_schema(tags=["SlideMicroscopyPost"])
class SlideMicroscopyPostViewSet(ModelViewSet):
    queryset = SlideMicroscopyPost.objects.all()
    
    def get_serializer_class(self):
        if self.action in ["list"]:            
            return SlideMicroscopyPostListSerializer
        elif self.action in ["retrieve"]:
            return SlideMicroscopyPostDetailSerializer
        return SlideMicroscopyPostWriteSerializer
    http_method_names = ["get", "post", "put", "delete"]
