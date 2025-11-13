from rest_framework import viewsets, permissions
from core.models import Post
from .serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Permissão customizada: só o autor pode editar/excluir
class IsAuthorOrReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['author']
	permission_classes = [IsAuthorOrReadOnly]
