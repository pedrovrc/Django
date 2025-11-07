from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Tarefa

class SessaoMiddlewareTest(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='teste', password='senha123')

	def test_acesso_sem_login_redireciona(self):
		response = self.client.get(reverse('lista_tarefas'))
		self.assertRedirects(response, '/accounts/login/?next=/tarefas/')

	def test_login_e_acesso_lista_tarefas(self):
		self.client.login(username='teste', password='senha123')
		response = self.client.get(reverse('lista_tarefas'))
		self.assertEqual(response.status_code, 200)

	def test_criar_tarefa_para_usuario_logado(self):
		self.client.login(username='teste', password='senha123')
		response = self.client.post(reverse('nova_tarefa'), {
			'titulo': 'Tarefa Teste',
			'descricao': 'Descrição da tarefa',
			'concluida': False
		})
		self.assertEqual(Tarefa.objects.count(), 1)
		tarefa = Tarefa.objects.first()
		self.assertEqual(tarefa.usuario, self.user)
		self.assertEqual(tarefa.titulo, 'Tarefa Teste')

	def test_editar_tarefa(self):
		self.client.login(username='teste', password='senha123')
		tarefa = Tarefa.objects.create(titulo='Original', descricao='Desc', usuario=self.user)
		response = self.client.post(reverse('editar_tarefa', args=[tarefa.id]), {
			'titulo': 'Editada',
			'descricao': 'Nova desc',
			'concluida': False
		})
		tarefa.refresh_from_db()
		self.assertEqual(tarefa.titulo, 'Editada')

	def test_excluir_tarefa(self):
		self.client.login(username='teste', password='senha123')
		tarefa = Tarefa.objects.create(titulo='Excluir', descricao='Desc', usuario=self.user)
		response = self.client.post(reverse('excluir_tarefa', args=[tarefa.id]))
		self.assertEqual(Tarefa.objects.count(), 0)

	def test_concluir_tarefa(self):
		self.client.login(username='teste', password='senha123')
		tarefa = Tarefa.objects.create(titulo='Concluir', descricao='Desc', usuario=self.user)
		response = self.client.get(reverse('concluir_tarefa', args=[tarefa.id]))
		tarefa.refresh_from_db()
		self.assertTrue(tarefa.concluida)
