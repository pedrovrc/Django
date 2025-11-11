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

**3. APIs e Integração** (Diretório `API`)
- ✅ Subprojeto já concluído.
- API REST para gerenciamento de tarefas, com autenticação JWT, filtros, documentação automática e frontend simples para consumo da API.

  **Como executar a aplicação:**
  1. Navegue até o diretório `API`:
	  ```powershell
	  cd API
	  ```
  2. Instale as dependências (caso ainda não tenha):
	  ```powershell
	  pip install django djangorestframework djangorestframework-simplejwt drf-yasg django-filter
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
  6. Obtenha o token JWT via endpoint:
	  ```powershell
	  curl.exe -X POST http://127.0.0.1:8000/api/token/ -H "Content-Type: application/json" -d "{\"username\":\"seu_usuario\", \"password\":\"sua_senha\"}"
	  ```
  7. Acesse os endpoints da API em [http://127.0.0.1:8000/api/tarefas/](http://127.0.0.1:8000/api/tarefas/), a documentação Swagger em [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) e o painel admin em [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).
  8. (Opcional) Abra o arquivo `frontend/index.html` para testar o consumo da API via frontend simples.

**4. Projeto Final** (Diretório `Projeto_Final`)
- 🟦 Próximo subprojeto a ser implementado.
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
