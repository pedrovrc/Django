from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Tarefa

# Create your tests here.
class TarefaAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teste', password='senha123')
        url = reverse('token_obtain_pair')
        response = self.client.post(url, {'username': 'teste', 'password': 'senha123'})
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_criar_tarefa(self):
        url = reverse('tarefa-list')  # rota do ViewSet
        data = {'titulo': 'API Teste', 'descricao': 'Teste', 'concluida': False}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Tarefa.objects.count(), 1)

    def test_listar_tarefas(self):
        Tarefa.objects.create(titulo='T1', usuario=self.user)
        url = reverse('tarefa-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_editar_tarefa(self):
        tarefa = Tarefa.objects.create(titulo='T1', usuario=self.user)
        url = reverse('tarefa-detail', args=[tarefa.id])
        data = {'titulo': 'Editada', 'descricao': 'Nova', 'concluida': True}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)
        tarefa.refresh_from_db()
        self.assertEqual(tarefa.titulo, 'Editada')

    def test_excluir_tarefa(self):
        tarefa = Tarefa.objects.create(titulo='T1', usuario=self.user)
        url = reverse('tarefa-detail', args=[tarefa.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Tarefa.objects.count(), 0)