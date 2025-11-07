## Projetos de Estudo - Django

Este repositório reúne quatro subprojetos criados para estudo e prática com o framework Django, seguindo um roadmap de aprendizado progressivo. Cada diretório representa um passo no aprendizado, cobrindo desde os fundamentos até tópicos avançados de deploy e boas práticas.

### Subprojetos

**1. Fundamentos do Django** (Diretório `Fundamentos`)
- ✅ Subprojeto já concluído.
- Mini Blog Pessoal simples com criação, edição e remoção de postagens.
- Objetivo de entender arquitetura, ciclo de requisição, padrão MTV, rotas, templates, migrations, ORM e painel administrativo do Django.

  **Como executar a aplicação:**
  1. Navegue até o diretório `Fundamentos`:
	  ```powershell
	  cd Fundamentos
	  ```
  2. Instale as dependências (caso ainda não tenha):
	  ```powershell
	  pip install django
	  ```
  3. Realize as migrações iniciais:
	  ```powershell
	  python manage.py migrate
	  ```
  4. (Opcional) Crie um superusuário para acessar o admin:
	  ```powershell
	  python manage.py createsuperuser
	  ```
  5. Execute o servidor de desenvolvimento:
	  ```powershell
	  python manage.py runserver
	  ```
  6. Acesse a aplicação em [http://127.0.0.1:8000/](http://127.0.0.1:8000/) e o painel admin em [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)


**2. Interatividade e Autenticação** (Diretório `Interatividade`)
- ✅ Subprojeto já concluído.
- App de tarefas com login, registro de usuário, edição, exclusão e marcação de tarefas como concluídas.
- Foco em integração de formulários, autenticação, permissões, feedback visual e estilização com Bootstrap.

  **Como executar a aplicação:**
  1. Navegue até o diretório `Interatividade`:
	  ```powershell
	  cd Interatividade
	  ```
  2. Instale as dependências (caso ainda não tenha):
	  ```powershell
	  pip install django
	  ```
  3. Realize as migrações iniciais:
	  ```powershell
	  python manage.py migrate
	  ```
  4. (Opcional) Crie um superusuário para acessar o admin:
	  ```powershell
	  python manage.py createsuperuser
	  ```
  5. Execute o servidor de desenvolvimento:
	  ```powershell
	  python manage.py runserver
	  ```
  6. Acesse a página inicial em [http://127.0.0.1:8000/](http://127.0.0.1:8000/) e o painel admin em [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

**3. APIs e Integração** (Diretório `API`)
- 🟦 Próximo subprojeto a ser implementado.
- API REST para gerenciamento de tarefas, com foco em utilizar o Django REST Framework (DRF)
- Uso de Serializers e ViewSets
- Rotas automáticas (DefaultRouter)
- CRUD completo via DRF
- Autenticação por token ou JWT (biblioteca djangorestframework-simplejwt)
- Permissões e filtros (usuário, status da tarefa)
- Testes de API
- Documentação automática via Swagger ou DRF-YASG
- Frontend simples (HTML/JS ou React) consumindo a API

**4. Projeto Final** (Diretório `Projeto_Final`)
- 🟨 Subprojeto ainda em fase de espera.
- Sistema de blog avançado com objetivo de aprender sobre estrutura modular, deploy e boas práticas
- Uso de organização modular (users, core, api, web)
- Autenticação completa (reset de senha, e-mail, etc)
- Integração com API REST para mobile/frontend
- Middleware customizado e signals
- Logging, cache e celery (tarefas assíncronas)
- Painel admin customizado
- Deploy (Gunicorn + Nginx ou Docker Compose)

---
Sinta-se à vontade para explorar, modificar e contribuir!
