## Projetos de Estudo - Django

Este repositório reúne quatro subprojetos criados para estudo e prática com o framework Django, seguindo um roadmap de aprendizado progressivo. Cada diretório representa um passo no aprendizado, cobrindo desde os fundamentos até tópicos avançados de deploy e boas práticas.

### Roadmap dos Subprojetos

**1. Fundamentos do Django** (Diretório `Fundamentos`)
- ✅ Subprojeto já concluído.
- Mini Blog Pessoal simples com criação, edição e remoção de postagens.
- Objetivo de entenderarquitetura, ciclo de requisição, padrão MTV, rotas, templates, migrations, ORM e painel administrativo do Django.

**2. Interatividade e Autenticação** (Diretório `Interatividade`)
- 🟦 Próximo subprojeto a ser implementado.
- App de tarefas com login, focando em integrar formulários, usuários e lógica de negócios.
- Uso de Django Forms e ModelForms
- Autenticação (login, logout, registro)
- CRUD de tarefas atreladas ao usuário autenticado
- Marcar tarefas como concluídas
- Sessões e Middleware
- Mensagens e redirecionamento (messages)
- Permissões básicas (@login_required)
- Estilização leve com Bootstrap

**3. APIs e Integração** (Diretório `API`)
- 🟨 Subprojeto ainda em fase de espera.
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
