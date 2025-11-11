from rest_framework import viewsets, permissions
from .models import Tarefa
from .serializers import TarefaSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class TarefaViewSet(viewsets.ModelViewSet):
    serializer_class = TarefaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['concluida']

    def get_queryset(self):
        # Retorna apenas as tarefas do usuário autenticado
        return Tarefa.objects.filter(usuario=self.request.user)
    
    def perform_create(self, serializer):
        # Associa a tarefa ao usuário autenticado ao criá-la
        serializer.save(usuario=self.request.user)