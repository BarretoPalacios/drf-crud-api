from .models import Proyectos
from rest_framework import viewsets, permissions
from .serializer import ProyectoSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyectos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProyectoSerializer 